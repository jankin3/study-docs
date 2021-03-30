# python time

## 主要作用

### 处理时间与日期

## 主要模块

### datetime

https://docs.python.org/zh-cn/3/library/datetime.html

- 常用的对象

	- date
	- time
	- datetime
	- timedelta,`时间换算常用`
	- tzinfo
	- timezone

### time

## 相互转化

### 字符串与时间对象

https://docs.python.org/zh-cn/3/library/datetime.html#strftime-strptime-behavior

- strptime() 

	- 作用：将对象转换为字符串
	- 方法类型：实例方法
	- 支持对象：	date; datetime; time
	- 使用，strftime(format)

- strftime()

	- 作用：将字符串解析为给定相应格式的 datetime 对象
	- 方法类型：类方法
	- 支持的类：datetime
	- 使用：strptime(date_string, format)

### 时间戳与时间对象

- 时间戳转化时间对象, datetime.fromtimestamp(timestamp, tz=None)
- 时间对象转化时间戳, datetime.timestamp()

*XMind: ZEN - Trial Version*