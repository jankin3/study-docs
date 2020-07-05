## 用户自定义类型

### 结构体

定义:聚合的数据类型

```go
//定义
type employee struct{
  age int
  name string
  address string
}

var a employee
b := employee{24, "jingwei", "Beijing"}
```

特点：

1. 通过点访问符号访问，a.name
2. 不允许含有自身类型的成员，但是允许含有自身类型成员的指针



### 类型

```go
type typeName 底层类型
// eg: type Celsius float64    // 摄氏温度
```

定义：创建一种新的数据类型，和现有底层的数据结构一致。用来分隔不同概念的类型，这样即使它们底层类型相同也是不兼容的

作用：

+ 分隔不同概念的类型, 避免表达式中的混用，会报错



### 方法

定义：方法和函数类似，区别是方法的意义是`给用户自定义的类型添加新的行为`。

使用：在函数的名之前加上接受者

```go
func (b employee) funcName (arge-List) (result-list) {
  // do-something
}
```

特点：

1. 函数的接受者，有两种，值接受者和指针接受者，其实也就是值传递和引用传递，但是go会自动转换，范例

   ```go
   // 并使用方法
   package main
   
   import "fmt"
   
   // user在程序里定义一个用户类型
   type user struct {
    name string
    email string
   }
   
   // notify使用值接收者实现了一个方法
   func (u user) notify() {
    fmt.Printf("Sending User Email To %s<%s>\n",
      u.name,
      u.email)
   }
   
   // changeEmail使用指针接收者实现了一个方法
   func (u *user) changeEmail(email string) {
    u.email = email
   }
   
   // main是应用程序的入口
   func main() {
    // user类型的值可以用来调用
    //使用值接收者声明的方法
    bill := user{"Bill", "bill@email.com"}
    bill.notify()
   
    // 指向user类型值的指针也可以用来调用
    // 使用值接收者声明的方法
    lisa := &user{"Lisa", "lisa@email.com"}
    lisa.notify()
   
    bill.changeEmail("bill@newdomain.com")
    bill.notify()
    lisa.changeEmail("lisa@newdomain.com")
    lisa.notify()
   }
   
   //output 
   Sending User Email To Bill<bill@email.com>
   Sending User Email To Lisa<lisa@email.com>
   Sending User Email To Bill<bill@newdomain.com>
   Sending User Email To Lisa<lisa@newdomain.com>
   ```



### 接口

定义：定义`行为`的类型

> “这些被定义的行为不由接口直接实现，而是通过方法由用户定义的类型实现。如果用户定义的类型实现了某个接口类型声明的一组方法，那么这个用户定义的类型的值就可以赋给这个接口类型的值”

特点：

1. 使用指针接受者实现的接口，必须传递指针

   ```
   Methods Receivers　　 Values
   -----------------------------------------------
   　 (t T)　　　　　　　　 T and *T
   　 (t *T)　　　　　　　　*T”
   ```

2. 多态，理解，不同的对象实现了相同的接口，不同的对象调用接口产生不同的行为





### 嵌入类型

定义：扩展或者修改已有类型的行为。理解类似于类的继承

作用：与内部类型相关的标识符会提升到外部类型上。这些被提升的标识符就像直接声明在外部类型里的标识符一样，也是外部类型的一部分

使用：

```go
type user struct{
  name string
  age int
}

type admin struct{
  user
  level int
}
```