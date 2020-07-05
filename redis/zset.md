# Redis 有序集合

定义: 和集合基本类似, 不同的是每个元素上关联一个score. 通过分数进行大小排序.

基本命令:

```shell
# 添加元素
zadd key score member
#元素累加
zincrby key int member
# 按照分数从大到小获取元素
zrevrange key start stop [withscores]
#按照分数区间获取元素
zrangebyscore key start stop
#移除
zrem key member
```



### 应用

- 排行榜

  主要用到了有序的特性, 以及对元素进行累加或者累减.

- 延时队列

  score存放到期时间,线程轮训处理