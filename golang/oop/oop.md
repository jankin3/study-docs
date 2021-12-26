# Golang的面向对象

## 什么是面向对象

解释：把相关的数据和方法组织为一个整体来看待，从更高的层次来进行系统[建模](https://baike.baidu.com/item/建模/814831)，更贴近事物的自然运行模式

## 面向对象的优点

+ 重用性
+ 灵活性
+ 扩展性



## 面向对象的三大特性

面向对象的特性主要有三个，封装，继承，多态。这里go是怎么实现的呢？

### 封装

解释：封装是把对象的属性私有化，提供一些外界可访问的属性或者方法。

go的实现方式有两种：

+ 大小写； 小写开头的变量属性方法只能在该包内程序中可见。是一个包级别的封装

+ 新的类型；可以通过 `type` 关键字创建新的类型，所以我们为了不暴露一些属性和方法，可以采用创建一个新类型的方式，自己手写构造器的方式实现封装，

  ```go
  type IdCard string
  
  func NewIdCard(card string) IdCard {
   return IdCard(card)
  }
  
  func (i IdCard) GetPlaceOfBirth() string {
   return string(i[:6])
  }
  
  func (i IdCard) GetBirthDay() string {
   return string(i[6:14])
  }
  ```

### 继承

解释：它可以使用现有类的所有功能，并在无需重新编写原来类的情况下对这些功能进行扩展。

golang也有两种方式来实现继承：

+ 内嵌匿名结构体类型：将父结构体嵌入到子结构体中，子结构体拥有父结构体的属性和方法，但是这种方式不能支持参数多态

- 内嵌匿名接口类型：将接口类型嵌入到结构体中，该结构体默认实现了该接口的所有方法，该结构体也可以对这些方法进行重写，这种方式可以支持参数多态，这里要注意一个点是如果嵌入类型没有实现所有接口方法，会引起编译时未被发现的运行错误。

```go
type Base struct {
    // 字段
}
type Derived struct {
    Base, // 嵌入
}
```

### 多态

解释：根据类型的具体实现采取不同的行为。

在`Go`语言中任何用户定义的类型都可以实现任何接口，所以通过不同实体类型对接口值方法的调用就是多态

```go
type SendEmail interface {
 send()
}

func Send(s SendEmail)  {
 s.send()
}

type user struct {
 name string
 email string
}

func (u *user) send()  {
 fmt.Println(u.name + " email is " + u.email + "already send")
}

type admin struct {
 name string
 email string
}

func (a *admin) send()  {
 fmt.Println(a.name + " email is " + a.email + "already send")
}

func main()  {
 u := &user{
  name: "asong",
  email: "你猜",
 }
 a := &admin{
  name: "asong1",
  email: "就不告诉你",
 }
 Send(u)
 Send(a)
}
```

GoLang的多态是依靠**`interface（接口）`**实现的。被具体的实例类型实例化后可以表现出实例类型的行为特征

golang父类与子类的覆盖问题:覆盖主要是子类使用同样的方法名来实现父类的方法

```go
package main

import "fmt"

type BaseBird struct {
    age int
}

func (this *BaseBird) Cal()  {
    this.Add()
}
func (this *BaseBird)Add()  {
    fmt.Printf("before add: age=%d\n", this.age)
    this.age = this.age + 1
    fmt.Printf("after add: age=%d\n", this.age)
}

type DerivedBird struct {
    BaseBird
}
func (this *DerivedBird) Add()  {
    fmt.Printf("before add: age=%d\n", this.age)
    this.age = this.age + 2
    fmt.Printf("after add: age=%d\n", this.age)
}

func main() {
    var b1 BaseBird
    var b2 DerivedBird

    b1 = BaseBird{age: 1}
    b1.Cal()

    b2 = DerivedBird{BaseBird{1}}
    b2.Cal()
}
```

思考一下输出的是什么？

结果：

```go
before add: age=1
after add: age=2

before add: age=1
after add: age=2
```

很明显，问题出在在BaseBird的Cal()方法中调用的依然是BaseBird的Add()方法。

为什么呢？

在GoLang所谓的“**继承**”的做法中，实际上是**匿名组合**。GoLang的组合是静态绑定，或者说GoLang所有的`struct`的方法都是静态绑定。所谓”父类“`BaseBird`的方法`Cal()`调用的本方法`Add()`，虽然在所谓”子类“`DerivedBird`中重新实现了`Add()`，但是对于”父类“的`Cal()`来说，在编译时期，就已经确定了他访问的是自己的`Add()`，也就是所谓“父类”`BaseBird`的。

回归来看GoLang。**如果我们在真实业务场景中，确实存在需要这种设计 - 公共逻辑中有一部分需要执行到不同具体类的逻辑 - 怎么办？**

一种做法是直接把实例作为参数再次传进入来实现多态：

```go
func (this *BaseBird) Cal(bird *BaseBird)  {
    bird.Add()
}
```

