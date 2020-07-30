# 字典排序

`问题，如何对字典进行按照值排序？`



思路：

go的字典的key是随机的，所以不可能在原结构上排序存储。所以这里方案是转化为结构体切片等其他结构

```go
type Pair struct {
	Key   string
	Value int
}

// A slice of Pairs that implements sort.Interface to sort by Value.
type PairList []Pair
```



方案一： 实现sort接口

```go
func (p PairList) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }
func (p PairList) Len() int           { return len(p) }
func (p PairList) Less(i, j int) bool { return p[i].Value < p[j].Value }

// A function to turn a map into a PairList, then sort and return it.
func sortMapByValue(m map[string]int) PairList {
	p := make(PairList, len(m))
	i := 0
	for k, v := range m {
		p[i] = Pair{k, v}
		i ++
	}
	sort.Sort(p)
	return p
}
```





方案二：切片排序方法sort.Slice() (文档：https://golang.org/pkg/sort/#Slice)

```go
func sortMapByValueV2(m map[string]int) (p PairList) {
	// to slice
	p = make(PairList, len(m))
	i := 0
	for k, v := range m {
		p[i] = Pair{k, v}
		i ++
	}

	sort.Slice(p, func(i, j int) bool {
		return p[i].Value > p[j].Value
	})
	return
}
```

