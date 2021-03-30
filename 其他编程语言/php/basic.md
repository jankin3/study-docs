# php 基础知识

### 编码解码

1. 检测编码

   mb_convert_detect($str, $array);

   mb_detect_encoding (  string $str [,  mixed $encoding_list = mb_detect_order() [,  bool $strict = false ]] )

2. 编码转换

   1. mb_convert_encoding (  string $str ,  string $to_encoding [,  mixed $from_encoding = mb_internal_encoding() ] )

   2. iconv ( string `$in_charset` , string `$out_charset` , string `$str` ) : string; 

      $out_charset可以添加参数;

      *//TRANSLIT*，将启用转写（transliteration）功能。这个意思是，当一个字符不能被目标字符集所表示时，它可以通过一个或多个形似的字符来近似表达

       *//IGNORE*，不能以目标字符集表达的字符将被默默丢弃

      否则出现错误会提示并返回false;



### 文件操作

fopen($filePath, $mode)-- 打开文件

file() -- 把整个文件读入一个数组中

fread ( resource `$handle` , int `$length` ) : string   读取文件

fgets() 从文件指针中读取一行

fclose() 关闭一个已打开的文件指针



### 正则表达式

```
preg_grep ( string $pattern , array $input [, int $flags = 0 ] ) 返回数组中匹配的栏目
```

```
preg_match ( string $pattern , string $subject [, array &$matches [, int $flags = 0 [, int $offset = 0 ]]] ) : int
// 执行正则表达式的匹配,返回匹配的次数(0或者1匹配到一次就终止), $matches是匹配的结果数组
//$matches[0]将包含完整模式匹配到的文本， $matches[1] 将包含第一个捕获子组匹配到的文本，以此类推
//如果发生错误preg_match()返回 FALSE。
```

```
preg_match_all 类似preg_match
```

```
preg_replace ( mixed $pattern , mixed $replacement , mixed $subject [, int $limit = -1 [, int &$count ]] ) : mixed
//执行一个正则表达式的搜索和替换, 
//如果匹配被查找到，替换后的subject被返回，其他情况下 返回没有改变的 subject。如果发生错误，返回 NULL 。
```

