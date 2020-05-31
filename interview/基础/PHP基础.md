### PHP基础
1. 单双引号的区别
2. 定义常量的几种方式
3. require、require_once、include的区别
4. 常见的array函数、string函数、排序函数
5. COW机制、引用的概念、函数的值传递和引用传递、
6. 变量容器zval
7. 垃圾回收机制
8. ==和===的区别、empty和isset的区别
   值为false的7种情况：0、'0'、false、NULL、''、0.0、[]
9. $_GLOBAL/$_SERVER/$_REQUEST/$_POST/$_GET/$_SESSION/$_COOKIE/$_FILES
10. curl、serialize、unserialize、get_memory_usage、json_encode...各种常用函数
11. 魔术变量、魔术方法、闭包、生成器、反射、
12. self, this和parent区别
13. PHP运行原理、PHP7新特性、PHP引擎是什么语言写的，结构了解吗
14. PHP支持多继承吗？
15. PHP连MySQL数据库的方法
16. php的数据类型



解答

1. 单引号认为是普通字符,双引号会解析变量略慢

2. define()函数和const关键字,

   + define()

     1. php执行阶段生效.效率略低,但是
     2. 灵活,比如表达式赋值等,复杂的变量名称,
     3. 不能再类中复制

   + const

     1. php编译阶段生效,效率高

     2. 不灵活, 不能在if里执行,  (原不可以赋值表达式,5.6之后可以),只能简单的常量名
     3. 可以再类中赋值

   总结,推荐使用const, 直观已读;效率快;

3. 核心功能都是引入外部文件;

   require:  要求,出错是致命错误

   require_once:之前已经引入过的不再引入,根据文件名

   include: 出错是警告

4. 常见的array函数、string函数、排序函数

   array_merge(), array_reverse(), array_reduce()

   str_replace(), strlen();strpos();substr()

   asort();

5. cow机制: 内存优化机制,相同的变量会使用同一块内存.比如

   ```php
   $a = 1;
   $b = $a; // 此时内存消耗没有增加,因为没有分配新的内存
   $a = 2; // 此时内存消耗增加,开始分配新的内存
   
   $a = 1;
   $b = &$a; // 此时内存消耗增加一点,是因为新的引用的数量
   $a = 2; // 此时内存消耗没有增加.
   
   ```

   引用:不同的变量指向同一块内容

   按值传递:不同的变量指向了不同的内容,

   引用传递: 不同的变量指向了相同的内容

6. 变量容器zval是实际存储变量的结构体.内容包括

   + 变量的值和变量的类型
   + is_ref是否是引用类型或者是普通类型
   + refcount,指向这个变量的个数

7. 垃圾回收机制
   + php5.3之前, 引用计数机制, 问题是循环引用
   + 之后, 在前面的基础上加上了根缓冲区,简单理解就是将发现的循环引用的zval放入缓冲区,达到一定数量之后清理

8. https://blog.csdn.net/miaosiwana/article/details/78094316

9. 三个等号是严格比较,包括数据类型,

   empty()只判断是否为空, 注意0,0.0之类也会被判断ture, isset() 是判断是否设置过变量

10. https://blog.csdn.net/qq_35458793/article/details/80651773

11. `魔术变量`: 两个__开头和结尾的称为魔术变量,比如dir,function, class, namespace

    `魔术方法`: 

    + construct,对象初始化的时候调用
    + destruct, 删除对象的时候或者对象终止的时候被调用
    + call/callstatic, 对象调用方法不存在的时候调用
    + get, 获取对象属性不存在的时候调用
    + toString 打印对象的时候调用
    + invoke,调用函数的方式调用一个对象时

`闭包`是没有名称的函数,一般当做参数使用

`生成器`, 优化内存使用,主要使用yield关键字实现

`反射`, 能拿到类里面的属性方法，private 和 protected的也可以, 目前用的不多

12. this指向了当前的对象,运行时实现, 可以访问属性和方法

    self指向了当前的类,类定义的时候实现,无关对象的建立,理论上只可以访问静态的资源,但是实际上可以通过当前的对象跨界访问动态的资源

    statis, 连接静态属性和静态方法

13. 运行原理:

    1. 边执行边编译
    2. zend引擎翻译php代码为一条一条机器码,然后执行

    php新特性:

    1. 三元表达式简化, ??
    2. define定义数组
    3. 函数的参数和返回结果的类型声明

    PHP引擎是c语言写的

14. 不支持多继承

15. PDO/mysqli

16. 静态类型 字符串,整数,浮点数,布尔,

    复合类型, 数据和对象