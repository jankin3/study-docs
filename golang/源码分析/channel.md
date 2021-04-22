# channel实现原理



Golang作为一门年轻的设计语言，golang最为人称道的就是可以随时随地开启协程。说到golang 的协程，不得不说golang 的设计思想：不要使用共享内存的方式进行通信，而是应该使用通信的方式去共享内存。



Go 语言提供了一种不同的并发模型，即通信顺序进程（Communicating sequential processes，CSP）[1](https://draveness.me/golang/docs/part3-runtime/ch06-concurrency/golang-channel/#fn:1)。Goroutine 和 Channel 分别对应 CSP 中的实体和传递信息的媒介，Goroutine 之间会通过 Channel 传递数据



所以channel到底是如何设计的呢？

考虑到有缓冲channel的消费者生产者模型。所以channel肯定含有队列

考虑到需要读写数据，肯定需要锁

考虑到需要记录等待接受和等待发送数据的goroutine，所以需要两个队列来存储等待的goroutine等