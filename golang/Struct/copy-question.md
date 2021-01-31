# Golang-结构体拷贝问题

问题：golang的结构体中的内部属性是浅拷贝还是深拷贝？

测试1，拷贝的dog中的属性

```go
package main

import "fmt"

type dog struct {
   tools []int
   foodNumMap map[string]int
   name string
}

func main(){
   d1 := dog{
      name: "pp",
      tools: []int{1,2,4},
      foodNumMap: map[string]int{
         "meat": 1,
         "fruit": 12,
      },
   }
   fmt.Printf("d1.toolPtr:%p||d1.foodNumMap:%p||d1.name:%p\n", d1.tools, d1.foodNumMap, &d1.name)

   d2 := d1 // 拷贝
   fmt.Printf("d2.toolPtr:%p||d2.foodNumMap:%p||d2.name:%p\n", d2.tools, d2.foodNumMap, &d2.name)
   d2.name = "jj"
   d2.tools[0] = 99
   d2.foodNumMap["meat"] = 100
   fmt.Printf("d1:%+v\n", d1)
   fmt.Printf("d2:%+v\n", d2)
}
//output
d1.toolPtr:0xc00001e100||d1.foodNumMap:0xc0000621b0||d1.name:0xc0000621a0
d2.toolPtr:0xc00001e100||d2.foodNumMap:0xc0000621b0||d2.name:0xc000062200
d1:{tools:[99 2 4] foodNumMap:map[fruit:12 meat:100] name:pp}
d2:{tools:[99 2 4] foodNumMap:map[fruit:12 meat:100] name:jj}
```

不难看出，结构体中的引用类型的拷贝实际是浅拷贝。修改d2的数据，d1的数据也会被修改。



### 测试2：结构体拷贝，长度增加

bytes包的Buffer结构体为什么地址相同但是数据却不同（在不扩容的时候）？

```go
import (
	"bytes"
	"fmt"
	"strconv"
	"strings"
	"sync"
)

var b = bytes.Buffer{}

func init(){
	stringA:= "hello"
	b.WriteString(stringA)
}

func test1(wgp *sync.WaitGroup, testStr string){
	defer wgp.Done()

	c := b
	c.WriteString(testStr)
	fmt.Printf("addr:%p||string:%+v||Bytes:%+v||real:%+v\n", c.Bytes(), c.String(), c.Bytes(), c)
	fmt.Printf("addr:%p||string:%+v||Bytes:%+v||real:%+v\n", b.Bytes(), b.String(), b.Bytes(), b)
}

func main(){
	test1(&wg, testStr)
}

// output
addr:0xc00001a140||string:hello0000000000000000000000000000000000000000000000000000000||Bytes:[104 101 108 108 111 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48]||real:{buf:[104 101 108 108 111 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48 48] off:0 lastRead:0}
addr:0xc00001a140||string:hello||Bytes:[104 101 108 108 111]||real:{buf:[104 101 108 108 111] off:0 lastRead:0}
```

c修改了buf的数据，但是原数据结构却没有变化？

解决：

结构体拷贝时实际拷贝的引用的地址，长度，容积属性。所以虽然c拷贝了b的中的切片。但是当c的切片长度增加的时候b的切片长度保持不变，所以数据不同





### 测试3， 并发修改slice时，并发不安全问题

