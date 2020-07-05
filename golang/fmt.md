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

