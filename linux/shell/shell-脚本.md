# shell 脚本

## 作用：处理用户和系统的交互

## 语法基础

详细请看https://www.cnblogs.com/skywang12345/archive/2013/05/30/3106570.html#a1

## 相关拓展

### 安全性

原文:http://www.ruanyifeng.com/blog/2017/11/bash-set.html

- 问题：

	- 目前shell 遇到错误不会自动暂停，会继续向下执行，这个其他python之类程序有很大不同，很可能产生和预期不一样的结果

- 解决:set command用来定制环境

	- -u 遇到不存在的变量报错(同-o nounset)
	- 错误处理

		- command || exit 1
		- -e:发生错误，就终止执行(同-o errexit)
		- 特殊对于管道命令

			- 特殊性：Bash 会把最后一个子命令的返回值，作为整个命令的返回值
			- set -o pipefail:个人理解是把管道内部命令抛出去然后外部-e 会捕获，所以对于管道内部其实还是会继续执行操作

	- -x 输出详细输入输出(同-o xtrace)
	- 汇总:

		- shell 内部：set -euxo pipefail（推荐）
		- 执行时：bash -euxo pipefail xxx.sh

### ssh交互

- 简介:ssh 不单可以登录，可以直接执行相关命令ssh nick@xxx.xxx.xxx.xxx "df -h"
- shell  中需要与remote server 交互

	- 简单命令

		- 可以直接放在后面,使用引号, 例如ssh  $remote_host "mysqldump -uxxx-pxxx xxx"
		-  缺点：(不能传递变量)

	- 复杂命令

		- 想要实现复杂的命令,可以写在外部脚本中
		- eg:ssh nick@xxx.xxx.xxx.xxx 'bash -s' < test.sh var1 var2

### 相关操作符

- https://blog.csdn.net/x1269778817/article/details/46535729

*XMind: ZEN - Trial Version*