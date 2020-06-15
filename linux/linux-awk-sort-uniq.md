# linux命令- awk, sort, uniq

### awk

作用: 文本处理命令,

原理: 依次读取每一行执行操作

格式: 

1. 简单版本

   ```shell
   awk {action} filename
   #example 
   awk '{print $1}' access.log
   ```

2. 完全版本

   ```shell
   awk {pattern action} filename
   # example 
   awk {if($2 == '404') print $1} access. log
   ```

参考: http://www.ruanyifeng.com/blog/2018/11/awk.html



### sort

每一行作为一个单位进行ascii比较，升序输出

```shell
-r 逆序
-n 当成数字比较
-k 指定哪一列来作为比较
-u 去重
```



### uniq

uniq 可检查文本文件中重复出现的行列。

```shell
-c count统计次数
-d 只显示重复的列
-u 只显示不重复的列
```





### 应用：

统计日志中出现次数前十的ip

```
cat access.log | awk '{print $1}' | sort | uniq -c | sort -k 1 -nr | head -n 10
```

