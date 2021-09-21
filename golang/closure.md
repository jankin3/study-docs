# 闭包函数

### 基本概念
闭包可以理解成“定义在一个函数内部的函数“


### 闭包内的变量
> 问题：闭包内使用外部的变量，此时是引用还是拷贝？

```go
func TestFuncVar1() {
	x, y := 1, 1
	fmt.Printf("outer||x=%p||y=%p\n", &x, &y)
	f := func(a int) {
		fmt.Printf("inner||x=%p||y=%p\n", &a, &y)
		return
	}

	f(x)
}
```
所以我们常见的defer如果使用直接print则是拷贝，如果使用闭包函数则是引用。


### 闭包的使用场景
todo