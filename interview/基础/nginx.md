# nginx
1. nginx的进程模型
2. nginx的反向代理功能是什么
3. nginx如何和php-fpm交互的（fast-cgi模块）
4. nginx的负载均衡配置了解吗，还了解哪些nginx配置
5. nginx如何处理并发请求的

解答:

1. 一个master 负责监控worker进程以及生成worker进程
2. 使用nginx接受外部的请求,然后转发到内部的其他服务器,接收到服务器的返回的返回之后返回给客户端
   + 隐藏了真实的服务器.安全性
   + 可以使用负载均衡,减轻负担加快速度
3. cgi
4. upstream, weight
5. 多进程+异步非阻塞方式