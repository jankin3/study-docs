# for 循环



### 概括

for循环是一种常见的语言结构，了解其具体实现有助于我们编写正确的代码



### 现象

思考下面一段代码的结果

1. 循环中修改内容

```go
aMap := map[int]int{
  1: 1,
  2: 2,
}
for i,v := range aMap{
  fmt.Println(i,v)
  aMap[3] =3
}
fmt.Println(aMap)
fmt.Println("-----------------")

bSlice := []int{1,2,3}
for i,v := range bSlice{
  fmt.Println(i,v)
  bSlice[1] = 666
  bSlice = append(bSlice, 4)
}
fmt.Println(bSlice)
fmt.Println("-----------------")

cArray := []int{1,2,3}
for i,v := range cArray{
  fmt.Println(i,v)
  cArray[1] = 666
  bSlice = append(bSlice, 4)
}
fmt.Println(cArray)

// output
2 2
3 3
1 1
map[1:1 2:2 3:3]
-----------------
0 1
1 666
2 3
[1 666 3 4 4 4]
-----------------
0 1
1 666
2 3
[1 666 3]

```

2. 循环中获取内容地址

```go
func main() {
	arr := []int{1, 2, 3}
	newArr := []*int{}
	for _, v := range arr {
		newArr = append(newArr, &v)
	}
	for _, v := range newArr {
		fmt.Println(*v)
	}
}

$ go run main.go
3 3 3
```



### for循环切片时

```go
ha := a
hv1 := 0
hn := len(ha)
v1 := hv1
v2 := nil
for ; hv1 < hn; hv1++ {
    tmp := ha[hv1]
    v1, v2 = hv1, tmp
    ...
}
```

在循环切片的时候，会先复制a到一个新的变量ha，然后hn记录他的长度，然后开始循环。回到最上面看到的循环中修改内容现象，修改原有长度内的内容是生效的，但是追加之后的结果是不会打印出来的。

在循环中获取内容地址时，Go 语言会额外创建一个新的 `v2` 变量存储切片中的元素，**循环中使用的这个变量 v2 会在每一次迭代被重新赋值而覆盖，赋值时也会触发拷贝**。



### for循环数组时

数组和切片一样，但是因为数组是值拷贝。所以我们及时修改原有长度内的内容也不会在循环打印中体现出来。



### for循环map时

```go
ha := a
hit := hiter(n.Type)
th := hit.Type
mapiterinit(typename(t), ha, &hit)
for ; hit.key != nil; mapiternext(&hit) {
    key := *hit.key
    val := *hit.val
}
```

循环map的时候也是先拷贝变量再循环，但是因为是引用而且不像切片能限制长度，所以修改都能在循环中体现出来。



### 总结

1. 使用for-range循环会在编译期间转换成经典的for循环。

2. 在循环数组，切片和map的循环时都是复制原有变量，以及长度（如果有）然后开始循环
3. 在循环时会使用新的变量来存储循环中的值，每一次迭代被重新赋值而覆盖，赋值时也会触发拷贝