# 如何关闭channel



>  场景： 多个生产者一个消费者的情况下，当消费协程从channel中拿到想要的结果后会结束消费并返回，这时生产者协程可能还在，如何正确的关闭channel？

​              

### 通道注意事项

1. 向一个已经关闭的通道发送数据会造成panic
2. 关闭已经关闭的通道会造成panic



### 常见解法 

1. 粗暴关闭，使用recover恢复
2. 使用sync.once 保证通道只会被关闭一次，但是注意事项1还是会发生。此种方式下也不适合
3. 另外使用一个关闭通道来发送关闭信号



这里详细看一下解法3：

```go
package main

import (
	"fmt"
)

var (
	pChan    = make(chan int, 10)
	stopChan = make(chan bool)
)

func main() {
	close_test1()
}

func close_test1() bool {
	// 生产者
	for i := 0; i < 5; i++ {
		go func(in int) {
			fmt.Printf("func:%v----\n", in)
			select {
			case <-stopChan:
				fmt.Printf("stopChan to stop1:%v\n", in)
				return
			default:
				fmt.Println("continue")
			}

			select {
			case <-stopChan:
				fmt.Printf("stopChan to stop2:%v\n", in)
				return
			case pChan <- in:
				fmt.Printf("send data to pChan:%v\n", in)
			default:
				fmt.Println("continue2")
			}
			return
		}(i)
	}

  // 消费者
	for res := range pChan {
		if res == 1 {
			close(stopChan)
			return true
		}
	}
	return false
}
```

我们使用了一个stopChan来让消费者通知关闭信号。注意这里没有直接关闭pChan，因为还是会存在向已经关闭的pChan中发送消息的风险。这里生产进程使用了两个select（已经关闭的stopChan可以被读取，将读到空值），前面一个select用来判断是否已经关闭从而中断流程，如果没有这个会导致下面的select会随机执行一个。



参考：https://gfw.go101.org/article/channel-closing.html

