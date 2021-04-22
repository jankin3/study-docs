# 新特点

（对比php，python）



### 字典取值

```go
a := map[int]string{1:"fasf", 2:"24234"}
b, ok := a[2]
fmt.Println(b, ok)
// "24234", true
c, ok := a[22]
// "", false
```

键不存在的情况下，其他语言会报错，但是go依然可以获取到值(每个类型的0值)，只是第二个参数会是false(无论是否获取第2个值)

