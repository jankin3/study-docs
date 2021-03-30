# docker

参考：https://yeasy.gitbooks.io/docker_practice/advanced_network/port_mapping.html

## 概览

### docker是什么

- Docker 属于 Linux 容器的一种封装，提供简单易用的容器使用接口

### 目的：提供运行环境

### 类比虚拟机

- 相同点

	- 都提供环境

- 不同点

	- docker 更加轻便轻量级

### 特点

- Docker 是服务器----客户端架构

## 基本组成元素

### 镜像，镜像是一些打包好的已有的环境，可以被用来启动和创建容器，本身不能被直接修改

### 容器，容器是镜像的实例化，是可以修改的，但是都是临时修改。

### 仓库，存储和分发镜像的地方

## 常用

### 常见命令

- 镜像

	- 创建镜像：docker image buid -t image_name .
	- 查看镜像：docker image ls
	- 拉取镜像：docker image pull xxxx

- 容器

	- 启动

		- 新建并启动：

			- docker container run image_name
			- 原理解释

				- 1. 检查本地是否存在指定的镜像，不存在就从公有仓库下载
				- 2. 利用镜像创建并启动一个容器
				- 3. 分配一个文件系统，并在只读的镜像层外面挂载一层可读写层
				- 4. 从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
				- 5. 从地址池配置一个 ip 地址给容器
				- 6. 执行用户指定的应用程序
				- 7. 执行完毕后容器被终止

		- 启动已终止的容器：docker container start

	- 列出容器：docker container ls (--all包括已经死掉的)
	- 终止容器：docker container kill container_id
	- 清理容器文件：docker container rm container_id
	- 进入容器(常用)：docker exec -it container_id bash 

	  -t 选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上， -i 则让容器的标准输入保持打开

### docker-compose

- 作用：管理多个 Docker 容器
- 模板文件(核心)

	- 控制镜像

		- 注意每个服务都必须通过 image 指令指定镜像或 build 指令（需要 Dockerfile）等来自动构建生成镜像。

- 常用操作

	- 启动

		- `docker-compose up`,非常有用，它将尝试自动完成包括构建镜像,创建服务，启动服务，并关联服务相关容器的一系列操作

	- 停止

		- docker-compose down 此命令将会停止 up 命令所启动的容器，并移除网络

## 进阶

### 制作镜像

一般情况下使用仓库的镜像就够了，但是当不满足使用的时候我们就可以自己制作镜像

- 方式一. docker commit，通过修改容器配置并保存形成新的镜像,(不推荐，原因黑箱操作，资源冗余)
- 方式二.dockerfile

	- 原理：把每一层修改、安装、构建、操作的命令都写入一个脚本，用这个脚本来构建、定制镜像
	- 模板文件命令

		- RUN，容器构建阶段执行的操作,
		- CMD，容器启动命令,用于指定默认的容器主进程的启动命令
		- ENTRYPOINT

			- 特点：类似于CMD操作
			- 作用：当指定了 ENTRYPOINT 后，CMD 的含义就发生了改变，不再是直接的运行其命令，而是将 CMD 的内容作为参数传给 ENTRYPOINT 指令
			- 为什么要这么设计呢？应用

				- 1.方便添加用户自定义参数
				- 2.应用运行前可以做一些准备工作

	- 构建镜像命令

		- `docker build -t image_name .`

		  注意，这里理解最后一个点，表示当前目录，上下文的意思。基于docker的c/s架构，当我们执行构建镜像的时候其实操作是在服务器端(Docker 引擎)中构建。但是这时需要本地的文件的时候，就有了上下文的作用，docker build会将该路径下的文件传到服务器端(所以位置很重要)。

		- 其他用法，docker build 还支持从 URL，tar 压缩包 ，标准输入等构建；

### 网络配置

- 原理与实现：主要通过 Linux 上的 iptables 防火墙来进行管理和实现，配置--iptables=true|false 是否允许 Docker 添加 iptables 规则
- 外部访问内部：主机端口映射
- 内部访问外部:容器要想访问外部网络，需要本地系统的转发支持

*XMind: ZEN - Trial Version*