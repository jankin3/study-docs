###　接口

### 1. 接口是什么？

+ 内容上，接口是一个类型type，它描述了一系列方法的集合

  ```go
  type a interface {
    Read(p, []byte) (n int, err error) // 接口中的方法
  }
  ```

  

+ 作用上(继承)

  一个实现了这些方法的具体类型就是这个接口的实例。

  也就是说，go中的继承是隐式继承，不像其他的语言显示implement 显式实现接口

### 2. 接口的特点

1. 可替换性

> 一个类型可以自由的使用另一个满足相同接口的类型来进行替换被称作可替换性(LSP里氏替换)。这是一个面向对象的特征

```go
package fmt

func Fprintf(w io.Writer, format string, args ...interface{}) (int, error)
func Printf(format string, args ...interface{}) (int, error) {
    return Fprintf(os.Stdout, format, args...)
}
func Sprintf(format string, args ...interface{}) string {
    var buf bytes.Buffer
    Fprintf(&buf, format, args...)
    return buf.String()
}
```

　上面，Printf()和Sprintf()都使用了Fprintf()的方法来实现,参数一第一个传入的是os.Stdout,第二个是bytes.Buffer, 为什么这两个不同的类型都可以传给io.Writer呢? 这就是因为他们都实现了io.Writer的writer 的write接口.



### 3.接口使用

1. 接口指定

   表达一个类型属于某个接口只要这个类型实现这个接口

   ```go
   var w io.Writer
   w = os.Stdout           // OK: *os.File has Write method
   w = new(bytes.Buffer)   // OK: *bytes.Buffer has Write method
   w = time.Second         // compile error: time.Duration lacks Write method
   
   var rwc io.ReadWriteCloser
   rwc = os.Stdout         // OK: *os.File has Read, Write, Close methods
   rwc = new(bytes.Buffer) // compile error: *bytes.Buffer lacks Close method
   ```

2. 空接口使用

   可以将任意值赋给空接口，因为空接口没有对实现类有任何要求

   ```go
   var any interface{}
   any = true
   any = 12.34
   any = "hello"
   any = map[string]int{"one": 1}
   any = new(bytes.Buffer)
   ```

   

### 4.实用注意

1. 接口只可以包含没有实现的方法，不能有变量
2. 实现接口要实现`所有`的方法
3. 只要是`类型type`，都可以实现结构体，不仅仅是结构体
4. 接口是一个`引用`类型



### 5. 使用场景

+ 使用已有的接口方法- 实例，结构体排序 

  1. 手写排序算法中的一种来实现排序
  2. 使用提供的排序方法sort.Sort()，但是需要先实现接口

  ```go
  package main
  
  import (
    "fmt"
    "math/rand"
    "sort"
  )
  
  type student struct {
    name  string
    score float64
  }
  
  type studentSlice []student
  
  func (s studentSlice) Len() int {
    return len(s)
  }
  
  func (s studentSlice) Less(i, j int) bool {
    return s[i].score < s[j].score
  }
  
  func (s studentSlice) Swap(i, j int) {
    s[i], s[j] = s[j], s[i]
  }
  
  func main() {
    sSlice := studentSlice{}
    for i := 0; i < 10; i++ {
        s := student{
            name:  fmt.Sprintf("pipi-%d", rand.Intn(1000)),
            score: rand.Float64(),
        }
        sSlice = append(sSlice, s)
    }
    fmt.Println("before")
    for _, item := range sSlice {
        fmt.Println(item)
    }
    sort.Sort(sSlice)
    fmt.Println("after")
    for _, item := range sSlice {
        fmt.Println(item)
    }
  }
  
  ```

  

### 6. 常用标准库接口

+ error

  + 源码实现

  ```go
  type error interface {
      Error() string
  }
  ```

  ```go
  package errors
  
  func New(text string) error { return &errorString{text} }
  
  type errorString struct { text string }
  
  func (e *errorString) Error() string { return e.text }
  ```

  + 使用

    1. 同一个new的错误不相等

    ```go
    fmt.Println(errors.New("EOF") == errors.New("EOF")) // "false"  
    ```

    2. fmt.Errorf封装了error.New()