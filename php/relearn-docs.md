# 重学php

### 1. 定义

PHP, Hypertext Preprocessor超文本预处理器

`特点`是可以嵌入到HTML中运行,所以尤其适合web开发

```html
<html>
    <head>
        <title>Example</title>
    </head>
    <body>

        <?php
        echo "Hi, I'm a PHP script!";
        ?>

    </body>
</html>
```

起始符和终结符分别是<?php 和 ?>

`作用`, 

+ web服务器脚本
+ 命令行脚本



### 2.数据类型

标量：布尔，字符串，整形，浮点数

复合类型：　数组，对象，callable(回调类型)

特殊：null和资源



### 3. 函数

 ##### 函数中的函数

```
<?php
function foo()
{
  function bar()
  {
    echo "I don't exist until foo() is called.\n";
  }
}

/* 现在还不能调用bar()函数，因为它还不存在 */

foo();

/* 现在可以调用bar()函数了，因为foo()函数
   的执行使得bar()函数变为已定义的函数 */

bar();

?>
```

PHP 中的所有函数和类都具有全局作用域，可以定义在一个函数之内而在之外调用，反之亦然。区别与python外部则不可以调用；

##### 返回值

```
<?php
declare(strict_types=1);

function sum($a, $b): int {
    return $a + $b;
}

var_dump(sum(1, 2)); //3
var_dump(sum(1, 2.5)); //Fatal error
?>
```

严格模式 也会影响返回值类型声明。在默认的弱模式中，如果返回值与返回值的类型不一致，则会被强制转换为返回值声明的类型。在强模式中，返回值的类型必须正确，否则将会抛出一个**TypeError**异常.

##### 可变函数

如果一个变量的后面有括号，php就会认为这是个函数去寻找该函数, 并且尝试执行它。可变函数可以用来实现包括回调函数，函数表在内的一些用途。

```php
<?php
function foo() {
    echo "In foo()<br />\n";
}
function bar($arg = '') {
    echo "In bar(); argument was '$arg'.<br />\n";
}

$func = 'foo';
$func();        // This calls foo()

$func = 'bar';
$func('test');  // This calls bar()

?>
```

### 4.类与对象

##### 访问控制

对属性或方法的访问控制，是通过在前面添加关键字 *public*（公有），*protected*（受保护）或 *private*（私有）来实现的。被定义为公有的类成员可以在任何地方被访问。被定义为受保护的类成员则可以被其自身以及其子类和父类访问。被定义为私有的类成员则只能被其定义所在的类访问

类属性必须定义为公有，受保护，私有之一。如果用 *var* 定义，则被视为公有。

类中的方法可以被定义为公有，私有或受保护。如果没有设置这些关键字，则该方法默认为公有。

##### 抽象类

定义：任何一个类，如果它里面至少有一个方法是被声明为抽象的，那么这个类就必须被声明为抽象的。

1. 不能被实例化

2. 被定义为抽象的方法只是声明了其调用方式（参数），不能定义其具体的功能实现。

3. 继承一个抽象类的时候，子类必须定义父类中的所有抽象方法

##### 接口

定义：指定了实现的类必须实现的哪些方法，但自己不需要方法的具体实现称为接口

1. 只有方法没有实现
2. 所有方法都是public的

##### Trait

Trait 是为类似 PHP 的单继承语言而准备的一种代码复用机制

特点：

1. 无法实例化
2. 使method可以水平组合
3. 和类相似
4. 也就是提供了类的多继承的特性

使用方法：

use traitName1, traitName2;	

##### 重载

php的重载不同于java中的同名方法但是参数不同；

而是通过魔术方法实现的；

__call()

__callStatics

__set()

__get()

__isset()

__unset()



##### 魔术方法

__sleep();  序列化的时候会调用此方法，主要用于清理之类的操作

__wakeup();同上，反序列化的时候调用

__toString(); 输出字符串的时候调用

__clone(); 当复制完成时，如果定义了 clone() 方法，则新创建的对象（复制生成的对象）中的 clone()方法会被调用，可用于修改属性的值（如果有必要的话）

##### 后期静态绑定

“后期静态绑定”。“后期绑定”的意思是说，*static::* 不再被解析为定义当前方法所在的类，而是在实际运行时计算的。也可以称之为“静态绑定”，因为它可以用于（但不限于）静态方法的调用

```php
<?php
class A {
    public static function who() {
        echo __CLASS__;
    }
    public static function test() {
        self::who(); // output: A
        statics::who(); // output: B
    }
}

class B extends A {
    public static function who() {
        echo __CLASS__;
    }
}

B::test();
?>
```

##### 对象的引用

PHP 的引用是别名，就是两个不同的变量名字指向相同的内容。在 PHP 5，一个对象变量已经不再保存整个对象的值。只是保存一个标识符来访问真正的对象内容。 当对象作为参数传递，作为结果返回，或者赋值给另外一个变量，另外一个变量跟原来的不是引用的关系，只是他们都保存着同一个标识符的拷贝，这个标识符指向同一个对象的真正内容。 

意思就是不是应用，但是其实指向的东西是一样的

```php
<?php
class A {
    public $foo = 1;
}  

$a = new A;
$b = $a;     // $a ,$b都是同一个标识符的拷贝
             // ($a) = ($b) = <id>
$b->foo = 2;
echo $a->foo."\n";


$c = new A;
$d = &$c;    // $c ,$d是引用
             // ($c,$d) = <id>

$d->foo = 2;
echo $c->foo."\n";


$e = new A;

function foo($obj) {
    // ($obj) = ($e) = <id>
    $obj->foo = 2;
}

foo($e);
echo $e->foo."\n";

?>
/*
output:
2
2
2
*/
```

##### 对象序列化

所有php里面的值都可以使用函数[serialize()](https://www.php.net/manual/zh/function.serialize.php)来返回一个包含字节流的字符串来表示。[unserialize()](https://www.php.net/manual/zh/function.unserialize.php)函数能够重新把字符串变回php原来的值。 序列化一个对象将会保存对象的所有变量，但是不会保存对象的方法，只会保存类的名字。

反序列化之前必须包含原本的类的定义



##### 命名空间

定义: 命名空间是封装的一种方法, 类似与操作系统的文件目录,不同的目录可以存在相同的文件.

解决了什么问题：

1. 用户编写的代码与PHP内部的类/函数/常量或第三方类/函数/常量之间的名字冲突。
2. 为很长的标识符名称(通常是为了缓解第一类问题而定义的)创建一个别名（或简短）的名称，提高源代码的可读性。

使用,类似目录:

1. 非限定名称, 例如 *$a=new foo();* 或 *foo::staticmethod();*。如果当前命名空间是 *currentnamespace*，foo 将被解析为 *currentnamespace\foo*

2. 限定名称, 例如 *$a = new subnamespace\foo();* 或 *subnamespace\foo::staticmethod();*。如果当前的命名空间是 *currentnamespace*，则 foo 会被解析为 *currentnamespace\subnamespace\foo*
3. 完全限定名称, 例如， *$a = new \currentnamespace\foo();* 或 *\currentnamespace\foo::staticmethod();*。在这种情况下，foo 总是被解析为代码中的文字名(literal name)*currentnamespace\foo

导入

允许通过别名引用或导入外部的完全限定名称,

```
use My\Full\Classname as Another;
```

##### 安全

sql注入攻击

防止: 

+ 数据库权限
+ 不要相信任何用户的输入
+ 对于所有用户输入的数据进行校验, 比如类型, 范围
+ 采用安全的查询机制, 比如tp中的数组查询而不是字符串查询



#####　垃圾回收

引用计数机制，

如果出现循环引用使用根缓冲区回收周期来模拟删除进行回收