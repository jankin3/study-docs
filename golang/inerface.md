# golang 高级属性

###　接口

#### 1. 可替换性

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



