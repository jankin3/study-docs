# HTTP

引用: https://juejin.im/entry/5981c5df518825359a2b9476

## 基本知识

### 应用层协议

### 客户端（用户）和服务端（网站）之间请求和应答的标准

##  发展

### http 1.0

### http 1.x 

- 改进之处

	- 缓存处理
	- 带宽优化及网络连接的使用

		- 允许只请求资源的某个部分

	- 错误通知的管理

		- 新增了24个错误状态响应码

	- Host头处理

		- HTTP1.1的请求消息和响应消息都应支持Host头域

	- 长连接

		- Connection： keep-alive

### http 2.0

- 基于google提出的SPDY
- 改进之处

	- 新的二进制格式
	- 多路复用(区别于长连接)
	- header压缩
	- 服务端推送

## 拓展

### https

- 是什么？

	- 超文本传输安全协议

- 过程

	- HTTPS经由HTTP进行通信，但利用SSL/TLS来加密数据包

- 区别

	- http:运行在TCP之上，所有传输的内容都是明文
	- https:运行在SSL/TLS之上，SSL/TLS运行在TCP之上，所有传输的内容都经过加密的

### tcp

*XMind: ZEN - Trial Version*