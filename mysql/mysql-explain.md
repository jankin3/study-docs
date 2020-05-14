# mysql explain

## 作用：sql查询如何执行，近似结果

## 相关

### explain extend

### explain partitions

## 主要行解释

### id

- 编号，

  标识select 所属行，id越大越先执行，id相同顺序执行

### select type

- 显示对应行是简单还是复杂查询

### type(访问类型)

- NULL
- const、system
- eq_ref
- ref
- range
- index

	- 全表扫描，按照索引

- ALL

	- 全表扫描，按行

### table

- 显示正在访问的表

### ken_len

- 索引使用字节数

### ref

### row

- 估计读取行数

### filtered

### extra

参考：https://www.cnblogs.com/kerrycode/p/9909093.html

- Using temporary
- Using filesort
- Using Index
- Using Index Condition
- Using where

*XMind: ZEN - Trial Version*