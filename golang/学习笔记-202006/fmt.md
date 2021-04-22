# fmt 输出

###　print-常用控制台打印
```go

func Print(a ...interface{}) (n int, err error)
//Print 使用其操作数的默认格式进行格式化并写入到标准输出。 当两个连续的操作数均不为字符串时，它们之间就会添加空格。 它返回写入的字节数以及任何遇到的错误。

func Printf(format string, a ...interface{}) (n int, err error)
//Printf 根据于格式说明符进行格式化并写入到标准输出。 它返回写入的字节数以及任何遇到的写入错误。

func Println(a ...interface{}) (n int, err error)
//Println 使用其操作数的默认格式进行格式化并写入到标准输出。 其操作数之间总是添加空格，且总在最后追加一个换行符。 它返回写入的字节数以及任何遇到的错误。

```



### Errorf -格式化输出错误

```go
func Errorf(format string, a ...interface{}) error
```



###　Sprint-返回字符串

```
func Sprint(a ...interface{}) string
func Sprintf(format string, a ...interface{}) string
func Sprintln(a ...interface{}) string
```



### Fprint-底层操作实现

```
func Fprint(w io.Writer, a ...interface{}) (n int, err error)
func Fprintf(w io.Writer, format string, a ...interface{}) (n int, err error)
func Fprintln(w io.Writer, a ...interface{}) (n int, err error)
```

以上的print()和Sprint()都是通过Fprint()实现，分别使用了os.Stdout和bytes.Buffer,

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





### 常用打印类型

1. 普通占位符 %v `常用`

```go
%v 打印值的默认形式, {zhangsan}，
%+v打印结构体的时候会打印字段名,{Name:zhangsan}
%#v打印go的语法表示,main.Human{Name:"zhangsan"}

%T 相应值的类型的Go语法表示
```



2. 整数占位符

   ```cpp
   占位符     说明                                  举例                       输出
   %b      二进制表示                             Printf("%b", 5)             101
   %c      相应Unicode码点所表示的字符              Printf("%c", 0x4E2D)        中
   %d      十进制表示                             Printf("%d", 0x12)          18
   %o      八进制表示                             Printf("%d", 10)            12
   %q      单引号围绕的字符字面值，由Go语法安全地转义 Printf("%q", 0x4E2D)        '中'
   %x      十六进制表示，字母形式为小写 a-f         Printf("%x", 13)             d
   %X      十六进制表示，字母形式为大写 A-F         Printf("%x", 13)             D
   %U      Unicode格式：U+1234，等同于 "U+%04X"   Printf("%U", 0x4E2D)         U+4E2D
   ```

3. 字符串与字节切片

   ```cpp
   %s      输出字符串表示（string类型或[]byte)   Printf("%s", []byte("Go语言"))  Go语言
   %q      双引号围绕的字符串，由Go语法安全地转义  Printf("%q", "Go语言")         "Go语言"
   %x      十六进制，小写字母，每字节两个字符      Printf("%x", "golang")         676f6c616e67
   %X      十六进制，大写字母，每字节两个字符      Printf("%X", "golang")         676F6C616E67
   ```

