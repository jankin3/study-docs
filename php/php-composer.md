# php-composer

## 定义

### php依赖管理工具，管理php项目所需要的项目依赖

### 问题，如何加载外部类?也就是如何引入外部依赖?

### 预备知识:

- 1.require/include
- 1.魔术方法__autoload, 当调用未定义的类的时候调用

## 原理

### 1. 主动使用require, include 引入

- 可以直接加载，缺点是性能代价高（启动即加载），以及包含不必要的类

### 2. __autoload()魔术方法

- 改进成了懒加载，解决了性能问题,缺点是此全局函数只能定义一次，不够灵活，并且加载所有的映射很复杂

### 3.  __autoload()的改进 spl_autoload_register()

-  改进使用堆栈的方式实现autoload()，实现统一管理。通俗的说，就是动态加载我们所需要的类文件
- spl_autoload_register ([ callable $autoload_function [, bool $throw = true [, bool $prepend = false ]]] ) : bool
将函数注册到SPL __autoload函数队列中。如果该队列中的函数尚未激活，则激活它们。
- 使用: 接受一个(闭包)函数作为第一个参数, 意思就是注册该该闭包函数作为一个autoload的具体实现, 但是可以注册多个函数,当遇到未定义的类的时候,循环调用此队列中的函数来实现引入

## 源码流程

### 1. 项目入口处一般require vendor/autoload.php

### 2. autoload_real.php下的getLoader()

### 3. 实例化$loader, 并根据环境获取对应配置参数,然后注册$loader, 也就是spl_autoload_register()注册了一个loadClass()的函数, 目的是加载外部类

## 依赖位置规范

### 概述:当解决了动态加载的问题之后，另一个问题是如何存放外部依赖的位置，不可能随意放让spl_autoload_register自己去注册一堆来加载

### 问题：如何合理存放外部依赖的位置并且易于查找？

### psr4/psr0/classmap

## 参考：

### https://mp.weixin.qq.com/s/yaPFxK92Cnw-UMBek5mIAA

### https://mp.weixin.qq.com/s/_OxtbSIlucUEYgNtXsZJmA

### https://segmentfault.com/a/1190000014948542

*XMind - Trial Version*