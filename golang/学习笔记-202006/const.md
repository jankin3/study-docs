# 常量

### 定义

在程序运行时，不会被修改的量。

常量中的数据类型只可以是布尔型、数字型（整数型、浮点型和复数）和字符串型。

```go
// single
const a = 2
const b int = 4

// more
const(
	a = 3
  c = "hello"
)

// 只允许内建表达式
const d = len(a)
```





### iota关键字（区别于itoa）

特殊常量，

iota 在 `const关键字出现时`将被重置为 0(const 内部的第一行之前)，const 中`每新增一行`常量声明将使 iota 计数一次(iota 可理解为 const 语句块中的行索引)。

```go
const (
	a = iota
	b = iota
	c = iota
)
// 省略写法
const(
	x = iota
	y
	z
)

func main() {
	fmt.Println(a, b, c)
	//output: 0 1 2
}
```



实例2

```go
package main

import "fmt"

func main() {
    const (
            a = iota   //0
            b          //1
            c          //2
            d = "ha"   //独立值，iota += 1
            e          //"ha"   iota += 1
            f = 100    //iota +=1
            g          //100  iota +=1
            h = iota   //7,恢复计数
            i          //8
    )
    fmt.Println(a,b,c,d,e,f,g,h,i)
}
```

