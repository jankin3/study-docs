### 面试问题



1. Struct 之间是否可以比较？
2. new和make的区别
3. golang的内存管理
4. goroutine原理和优势
5. 每个协程和线程占用的内存
6. 反射使用以及原理
7. Redis分布式锁
8. redis模式



答案：

1. 根据结构体中的值的数据类型决定，如果结构体中的属性可以比较则可以比较，否则不可以。在编译期已决定。

2. 都是用来分配内存。
   + 使用对象不同，new可以适用任何对象，但是make只适用于引用类型。
   + 返回值不同，new返回地址，make返回初始化后的结构

3. 内存管理

   1. 内存分配方式：

   + 堆内存，用于动态分配内存，gc回收内存
   + 栈内存，函数调用时存储的局部变量，主要通过出栈和入栈来内存分配和释放
   + 其他静态分配

   + 堆内存分配比栈内存分配昂贵，因为栈内存管理只用入栈和出栈
   + 内存逃逸是指原本应该在栈上分配的内存最终到堆上分配
     + 当发送指针到channel中
     + 切片中含有指针
     + slice扩容
     + interface类型上调用方法

   2. 垃圾回收。三色标记法，分为白色，灰色，黑色三个颜色集合。

      1. 把所有对象放到白色集合中
      2. 从根节点开始遍历，所有的引用放到灰色集合
      3. 遍历灰色集合，灰色集合的引用放到黑色集合。遍历过的放到黑色集合
      4. 循环上面三步直到灰色集合没有对象，则白色集合就是垃圾

4. lue

5. lue

6. 反射是在运行时动态的获取对象的属性和方法。一般使用reflect包，去获取对象的type和value，然后获取更多的属性和方法

7. 获取锁的时候简单，但是当释放锁的时候需要注意，可能自己的锁已经超时释放了，释放掉了其他协程的锁，这时需要注意对比val值来释放。

8. 主从模式 可以实现读写分离，数据备份。但是并不是「高可用」的

   哨兵模式 可以看做是主从模式的「高可用」版本，其引入了 Sentinel 对整个 Redis 服务集群进行监控。但是由于只有一个主节点，因此仍然有写入瓶颈。

   Cluster 模式 不仅提供了高可用的手段，同时数据是分片保存在各个节点中的，可以支持高并发的写入与读取。当然实现也是其中最复杂的。