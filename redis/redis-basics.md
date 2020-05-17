# redis基础

## 简介

### 高性能key-value数据库

### 优势

- 丰富的数据结构
- 性能极高，读11w/s,写8w/s

## 数据类型

### 字符串

- 存储值或者获取值set/get

### 哈希

- 设置获取判断存在HMSET/HGET/HEXISTS

### 列表

- 头部插入, 弹出元素，获取范围元素 LPUSH/LPOP/LRANGE

### 集合

- 添加元素，判断元素是否存在，取交集， SADD/SISMEMBER/SDIFF

### 有序集合

- 每个成员都有一个分数，	ZADD key score1 member1

### 使用相关

- php

	- tp，S() 实际存储的是字符串类型，如果需要其他类型，需要自己实例化redis原生对象
	- laravel，Facades\Redis可以调用原生的redis操作，但是封装的cache接口就不行
	- phpredis && predis

		- 两者都是php的redis客户端，phpredis使用的c编写，predis使用php编写，性能在量级大的情况下可能会有偏差。

## 命令相关

### 配置修改

- 热修改:config set
- 修改配置文件，重启生效

### 客户端

- redis-cli

### 持久化

- RDB

	- 概括：直接快照redis数据到xxx.rdb文件
	- 工作原理

		- 1.通过fork一个子进程，，然后
		- 2.快照数据到rdb文件
		- 3.rename替换掉旧的rdb文件

	- 特点：单文件，适合备份，启动较快，但是容易丢失数据

- AOF

	- 概括：记录redis的每一次的操作，通过重复执行一次来持久化
	- 特点：稳定，默认每秒执行一次，意味着最多丢失1s的数据，但是文件一般比较大

*XMind - Trial Version*