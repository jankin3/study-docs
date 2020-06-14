# PHP 时间与日期

### 获取指定时间

#####　1. 获取指定时间的时间戳

strtotime(); 将指定的字符串转换程时间戳;

```
echo strtotime("+1 day"), PHP_EOL;
echo strtotime("+1 week"), PHP_EOL;
echo strtotime("+1 week 2 days 4 hours 2 seconds"), PHP_EOL;
```

##### 2. 转化为时间

date() 函数

用法date(format[,timestamp]),第一个参数是格式,第二个参数是时间戳,默认是当前的时间戳



### 时间字符串与时间戳转换

strtotime(); 字符串转换时间戳

date();　时间戳转换字符串