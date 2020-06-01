# php-composer

## 是什么？

### 依赖管理工具，管理php项目所需要的项目依赖

## 加载

### 问题，如何从命名空间直接找到类的类的文件并加载？

### 原理

- 1. 使用require, include ，可以直接加载，缺点是性能代价高（启动即加载），以及包含不必要的类
- 2. __autoload()魔术方法, 改进成了懒加载，解决了性能问题,缺点是此全局函数只能定义一次，不够灵活，并且加载所有的映射很复杂。
- 3. spl_autoload_register(), 改进使用堆栈的方式实现autoload()，实现统一管理。通俗的说，就是动态加载我们所需要的类文件

## 外部依赖位置规范

### 概述:当解决了动态加载的问题之后，另一个问题是如何存放外部依赖的位置，不可能随意放让spl_autoload_register自己去注册一堆来加载

### 问题：如何合理存放外部依赖的位置并且易于查找？

### psr4/psr0/classmap

## 参考：

### https://mp.weixin.qq.com/s/yaPFxK92Cnw-UMBek5mIAA

### https://mp.weixin.qq.com/s/_OxtbSIlucUEYgNtXsZJmA

### https://segmentfault.com/a/1190000014948542

*XMind - Trial Version*