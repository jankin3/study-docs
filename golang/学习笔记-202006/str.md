# 字符串

### string

> type string
>
> string is the set of all strings of 8-bit bytes, conventionally but not necessarily representing UTF-8-encoded text. A string may be empty, but not nil. Values of string type are immutable.
>
> 文本字符串通常被解释为采用UTF8编码的Unicode码点（rune）序列

底层结构

```go
type stringStruct struct {
    str unsafe.Pointer
    len int
}
```



### []byte

概括：byte是uint8的别名



### []byte与string

1. string可以直接比较，而[]byte不可以，所以[]byte不可以当map的key值。
2. 因为无法修改string中的某个字符，需要粒度小到操作一个字符时，用[]byte。
3. string值不可为nil，所以如果你想要通过返回nil表达额外的含义，就用[]byte。
4. []byte切片这么灵活，想要用切片的特性就用[]byte。
5. 需要大量字符串处理的时候用[]byte，性能好很多。





### 字符串的遍历

先看一个例子

```go
str := "Hi,世界"
for i := 0; i < len(str); i++ {
  ch1 := str[i]
  ctype := reflect.TypeOf(ch1)
  fmt.Println(ch1, ctype)
}
fmt.Println("=============>")
for _, ch2 := range str {
  ctype2 := reflect.TypeOf(ch2)
  fmt.Println(ch2, ctype2)
}
```

思考输出，

```go
//output
72 uint8
105 uint8
44 uint8
228 uint8
184 uint8
150 uint8
231 uint8
149 uint8
140 uint8
=============>
72 int32
105 int32
44 int32
19990 int32
30028 int32
```

打印的是一串数字，说明字符串的底层是一堆byte字节存储。

打印类型，ch1为uint8，是byte类型。ch2为uint32，是rune类型。也就是使用range时，会解码为rune类型。

所以打印字符串方式，

```go
for _, ch2 := range str {
	fmt.Println(string(ch2))
}
```



### 字符串的长度

1. 单字节字符， len()

2. 多字节字符
   + len([]rune(s)), 强转为rune
   + utf8.RuneCountInString(s)
   + strings.Count(s, "")-1