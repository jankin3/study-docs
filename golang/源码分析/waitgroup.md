# waitGroup

### 使用场景

sync.WaitGroup可以等待一组 Goroutine 的返回，一个比较常见的使用场景是批量发出 RPC 或者 HTTP 请求

```go
requests := []*Request{...}
wg := &sync.WaitGroup{}
wg.Add(len(requests))

for _, request := range requests {
    go func(r *Request) {
        defer wg.Done()
        // res, err := service.call(r)
    }(request)
}
wg.Wait()
```

问题：如果你来设计waitGroup，你会怎么设计？

共享一个变量counter，add加，done减少，wait循环等待？

too young too sample



### 底层结构

首先看一下wg的结构

```go
type WaitGroup struct {
	noCopy noCopy // 防止拷贝，具体细节先忽略
	state1 [3]uint32 
}
```

state1占用12个字节，64位机器上， 官方解释

> 64-bit value: high 32 bits are counter, low 32 bits are waiter count，and the other 4 bytes as storage for the sema.

具体来讲就是存放了三个变量，

1. counter计数器，负责add和done的加减

2. waiter 负责存储等待的goroutine

3. sema存放信号量

   

### 主要方法

wg提供了三个对外的方法。Add(),Done(),Wait()

#### Add

```go
func (wg *WaitGroup) Add(delta int) {
	statep, semap := wg.state()
	state := atomic.AddUint64(statep, uint64(delta)<<32) // 对counter 加减
	v := int32(state >> 32) // 获取counter
	w := uint32(state) // 获取等待的goroutine的数量
	if v < 0 {
		panic("sync: negative WaitGroup counter")
	}
	if v > 0 || w == 0 { 
		return
	}
	*statep = 0
	for ; w != 0; w-- {
		runtime_Semrelease(semap, false, 0) // 循环一次，唤醒一个等待的goroutine
	}
}
```

Done只是简单的对Add的封装，传入-1



#### Wait方法

```go
func (wg *WaitGroup) Wait() {
	statep, semap := wg.state()
	for {
		state := atomic.LoadUint64(statep)
		v := int32(state >> 32)
		if v == 0 {
			return
		}
		if atomic.CompareAndSwapUint64(statep, state, state+1) {
			runtime_Semacquire(semap) // 调用陷入睡眠
			if +statep != 0 {
				panic("sync: WaitGroup is reused before previous Wait has returned")
			}
			return
		}
	}
}
```

当 wg 的计数器归零时，陷入睡眠状态的 Goroutine 会被唤醒，上述方法也会立刻返回。



总结，

wg 使用add 累计增加counter，并在counter为0时唤醒等待的协程，

使用done方法减少counter标记goroutine的完成，

调用wait判断是当前协程陷入睡眠。中间使用信号量来唤醒和等待