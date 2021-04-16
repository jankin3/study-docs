# Epoll 概览

### epoll 是什么？

io多路复用模型



### epoll原理

当请求来的时候，进程直接将就绪的socket放到就绪链表中，进程可以直接读取到已就绪的socket，所以相比与select更加快速



### select，epoll 对比

#### 共同点

select和epoll都是为了解决单进程能同时监听多个socket的场景。

#### select解决方案

建立一个列表存放socket，当socket就绪时开始遍历列表获取已就绪的socket

代码如下

```c
int s = socket(AF_INET, SOCK_STREAM, 0);  
bind(s, ...)
listen(s, ...)

int fds[] =  存放需要监听的socket

while(1){
    int n = select(..., fds, ...)
    for(int i=0; i < fds.count; i++){
        if(FD_ISSET(fds[i], ...)){
            //fds[i]的数据处理
        }
    }
}
```

select存在问题：

1. 最大容量问题，list最多只能容纳1024个
2. fd列表建立之后需要拷贝到内核中去监听
3. 当存在socket就绪的时候，不会告诉你具体是哪一个，需要自己遍历



#### epoll

当中断进程向socket写入数据的时候，会将已就绪的socket放入到epoll对象维护的就绪链表中，这样进程就可以直接能获取到已经就绪的socket。

```c
int s = socket(AF_INET, SOCK_STREAM, 0);   
bind(s, ...)
listen(s, ...)

int epfd = epoll_create(...);
epoll_ctl(epfd, ...); //将所有需要监听的socket添加到epfd中

while(1){
    int n = epoll_wait(...)
    for(接收到数据的socket){
        //处理
    }
}
```



