# nginx

## 是什么？

### web 服务器(也可负载均衡，反向代理)

## 特点

### 采用异步事件驱动，可大量并行处理

- linux 采用epoll 模型

  epoll模型基于事件驱动机制，它可以监控多个事件是否准备完毕，如果OK，那么放入epoll队列中，这个过程是异步的。worker只需要从epoll队列循环处理即可

### 模块化设计

- 丰富的第三方模块

## 配置

### 配置语法

- 块配置 event,http, server
- 配置项

	- 格式: 多个值用空格隔开
	- 单位：通用单位
	- 变量：少数模块支持，同php

### location

https://segmentfault.com/a/1190000013267839

- 作用: 根据url匹配对应处理规则
- 语法规则

	- location [ = | ~ | ~* | ^~ ] uri { ... }
location @name { ... }

- 匹配规则

	- 前缀匹配

		- = 表示精确匹配
		- ^~ 表示如果该符号后面的字符是最佳匹配，采用该规则，不再进行后续的查找
		-  字符串 会相互比较选择匹配度最高的, 一般配合PHP直接使用 location / 转换到php程序

	- 正则匹配

		- ~区分大小写
		- ~* 不区分大小写

### 基本配置

- debug 配置
- 正常运行的配置

	- env|env=value定义环境变量 (没怎么用过)
	- include,嵌入其他配置, 便于模块化
	- pid: master 进程ID的pid文件存放路径
	- user username groupname, worker 进程运行的用户以及用户组
	- worker_rlimit_nofile limit, 可以打开的最大文件句柄数
	- worker_rlimit_sigpending limit, 限制信号队列

- 优化性能配置

	- worker_processes number,worker 进程个数
	- worker_cpu_affinity cpumask, 绑定worker 进程到cpu内核
	- ssl 硬件加速
	- 系统调用gettimeofday 的评率
	- worker 进程优先级

- 时间类配置项

	- accept锁相关
	- lock 文件路径
	- 批零建立新连接
	- 选择时间模型
	- 每个worker 的最大连接数

### 配置分类

- 虚拟主机与请求的分发
- 文件路径的定义
- 内存以及磁盘的分配
- 网络连接的设置
- MIME类型的设置
- 对客户端请求的限制
- 文件操作的优化
- 对客户端请求的特殊处理

*XMind: ZEN - Trial Version*