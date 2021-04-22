# 如何控制并发



### waitgroup

`WaitGroup` 对象内部有一个计数器，最初从0开始，它有三个方法：`Add(), Done(), Wait()` 用来控制计数器的数量。`Add(n)` 把计数器加上`n` ，`Done()` 每次把计数器`-1` ，`wait()` 会阻塞代码的运行，直到计数器地值减为0。

```go
wg := sync.WaitGroup{}
	wg.Add(10)
	for i:=0;i<10;i++{
		go func(i int) {
			fmt.Println(i)
			wg.Done()
		}(i)

	}
	fmt.Println("wait")
	wg.Wait()
	fmt.Println("end")
```

注意：

1. wg不可以为复数

2. wg非引用，需要传递地址

   ```go
   func main(){
   	wg := sync.WaitGroup{}
   	wg.Add(10)
   	for i:=0;i<10;i++{
   		go gf(i, &wg)
   	}
   	fmt.Println("wait")
   	wg.Wait()
   	fmt.Println("end")
   }
   
   func gf(i int, wg *sync.WaitGroup){
   	defer wg.Done()
   	fmt.Println(i)
   }
   ```

   

### chan

概括：goroutine之间发送信号的通道

特点：

 1. 通道的收发操作在不同的两个 goroutine 间进行。

 2. 发送会`阻塞`直到被接受

 3. 接受将`阻塞`直到通道有数据

    + 阻塞接受

      ```go
      data := <-ch
      ```

    + 阻塞接受,当通道关闭之后ok为false

      ```go
      data, ok := <-ch
      //data：表示接收到的数据。未接收到数据时，data 为通道类型的零值。
      //ok：表示是否接收到数据。
      ```

类别： 

1. 无缓冲区管道，

   特点：

   1. 没有任何能力保存任何值
   2. 接受和发送必须同时准备好，才能完成。否者先开始者则等待

   实例：play badminton

   ```go
   // play ball
   package main
   
   import (
   	"fmt"
   	"math/rand"
   	"sync"
   	"time"
   )
   
   func init(){
   	rand.Seed(time.Now().UnixNano())
   }
   
   func main(){
   	wg := sync.WaitGroup{}
   	wg.Add(2)
   
   	court := make(chan int)
   	go play(court,"juju", 8, &wg)
   	go play(court, "pipi", 8, &wg)
   
   	court <- 0
   
   	wg.Wait()
   	fmt.Println("end")
   }
   
   func play(court chan int, name string, rate int, wgp *sync.WaitGroup){
   	defer wgp.Done()
   
   	for{
   		ball, ok := <- court
   		if !ok {
   			fmt.Println(name," is win")
   			break
   		}
   		randNum := rand.Intn(10)
   		if randNum > rate{
   			// fail
   			fmt.Println(name," is miss")
   			close(court)
   			return
   		}
   
   		ball ++
   		fmt.Println(name, "is play ball:", ball)
   
   		court <- ball
   	}
   }
   ```

   

   

### 死锁问题