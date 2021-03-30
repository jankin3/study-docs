# 字符串编码

发展与概述文章http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html

## 意义:使机器认识不同的字符串

## 编码分类与发展

ps:utf-8是Unicode的一种实现方式,从计算机工作方式来说一般在utf-8是用来存储和传输，unicode 一般用来转换

### ASCII

- 英语字符和二进制位对应

### unicode

- 所有的字符对应二进制位

### utf-8

- 以变长方式实现了unicode编码

## 其他

### python2 编码问题

细节请看：https://www.jianshu.com/p/58d5f64813dc

- type:str与unicode

	- str 是Unicode经过编码的字节
	- 真正的字符串

- 编码解码错误

	- python 会隐式地进行编码、解码，默认采用 ascii

- 类型转换

	- 2种类型的字符串都提供了 encode 和 decode 方法，通过类型转换解决问题

*XMind: ZEN - Trial Version*