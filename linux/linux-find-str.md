# Linux查找文本中的字符串

### 问题, 如何查找文件内容中带有某个字符串的文本?

### 1. grep 查找文本中符合条件的字符串

```
grep [args]  keywords ［文本或者目录］
如果没有指定文本或者目录，则从标准输入获取
常用：
-r recursive 递归目录去查找
-v 反向查找
-l 显示行号
-w 匹配全词
例子：
# 查找log 文件中含有test
grep test *.log
```



###  2. find指定目录查找文件

```
-name　指定文件名
-iname 不区分大小写
-type 指定类型　d/f 目录与普通文件
-atime/mtime/ctime 
-perm 执行权限
```



总结方法是：

1. grep -r keyword filepath
2. find . -name filename |xargs grep keyword (主要还是grep....)



