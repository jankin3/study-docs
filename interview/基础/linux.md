# Linux
1. 尽可能多地说出知道的Linux命令
2. 如何查看端口号被哪个进程占用
3. top/ps/netstat/tcpdump
4. IO模型了解哪些
5. 了解Linux文件系统吗



解答：

1. + 基本：cd, ls, 
   + 权限: chown chmod
   + 网络: netstat, ping, lsof -i:80
   + 进程查看: ps aux| grep xxx
   + 资源使用:du, df,

2.  lsof -i:port, netstat -ntlp | grep 8080
3. tcpdump: 监视网络资源
4. + 同步模型（synchronous IO）
   + 阻塞IO（bloking IO）
   + 非阻塞IO（non-blocking IO）
   + 多路复用IO（multiplexing IO）
   + 信号驱动式IO（signal-driven IO）
   + 异步IO（asynchronous IO）

5. inode 和block

