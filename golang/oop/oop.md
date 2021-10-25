# go的面向对象



## 三大特性

面向对象的特性主要有三个，封装，继承，多态。这里go是怎么实现的呢？

### 封装

GoLang中没有**`public`**、**`protected`**和**`private`**语法关键字，它是通过**大小写字母**来控制可见性的。如果常量、变量、类型、接口、结构、函数等名称是**以大写字母开头**则表示能被其它包访问，其作用相当于**`public`**，**以非大写开头**就则不能被其他包访问，其作用相当于**`private`**，当然，在同一个包内是可以访问的。

### 继承

这里区别就来了。go没有传统的implements等命令，而是使用嵌入来进行继承

```go
type Base struct {
    // 字段
}
type Derived struct {
    Base, // 直接嵌入即可
}
```

### 多态

GoLang的多态是依靠**`interface（接口）`**实现的。被具体的实例类型实例化后可以表现出实例类型的行为特征





## 一个问题

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

一种做法是直接把实例作为参数再次传进入。。。

```go
func (this *BaseBird) Cal(bird *BaseBird)  {
    bird.Add()
}
```

