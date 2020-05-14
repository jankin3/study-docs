# java学习

## 概览

### 是什么?

- 介于编译型语言和解释型语言之间一门编程语言

### 特点

- 一次编写，到处运行， 即跨平台

### 有什么？

- 版本

	- Java EE：Enterprise Edition
	- Java SE：Standard Edition
	- Java ME：Micro Edition

- 名词解释

	- JVM：java virtual machine
	- JDK：Java Development Kit
	- JRE：Java Runtime Environment

### 对比

- 语言类型拓展解释

	- https://www.zhihu.com/question/19918532
	- 强、弱类型

		- 简单的说就是，弱类型语言，类型检查更不严格

	- 动态、静态类型

		- statically, 编译时报错
		- dynamiclly, 运行时报错

- 结果

	- C/C++， 弱类型，statically
	- python，强类型，dynamiclly
	- PHP，弱类型，dynamiclly

## 基础

### 代码结构

- 一个程序的基本单位就是class, class 中有若干个类

### 变量和数据类型

- 先定义后使用
- 基本数据类型

	- 整数类型：byte，short，int，long
	- 浮点数类型：float，double
	- 字符类型：char
	- 布尔类型：boolean

- 引用类型

	- 字符串
	- 数组

		- 数组所有元素初始化为默认值，整型都是0，浮点型是0.0，布尔型是false；
		- 数组一旦创建后，大小就不可改变

- 常量

	- 如果加上final修饰符，这个变量就变成了常量

### 面向对象

- 基本概念

	- 类
	- 实例
	- 方法

- 基本实现

	- 继承
	- 多态

### 反射

- 通过Class实例获取class信息的方法称为反射(Reflection)

### 集合

- 结构

	- Collection

		- List

			- ArrayList
			- LinkedList

		- Set

	- Map

*XMind: ZEN - Trial Version*