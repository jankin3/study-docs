# Redis
1. 知道哪些redis数据类型？各自的应用场景是什么？内部实现的数据结构知道吗？
2. 常见redis操作命令
3. redis线程模型
4. redis为什么速度快
5. redis事务了解吗？
6. redis哨兵和集群了解吗
7. redis的内存淘汰机制
8. redis持久化机制了解吗
9. redis主从复制的过程是什么
10. 什么是缓存穿透、击穿、雪崩？如何解决？
11. redis如何实现zset
12. 如何解决数据库、redis更新数据不一致的问题
13. 如何用redis实现分布式锁



1. 1. 字符串, 基本类型,缓存使用; SDS
   2. 散列表, 缓存字典类型的数据, ziplist 和hashtable
   3. 数组, 栈, 队列使用, 消息队列,使用双向链表, ziplist和hashtable
   4. 集合,缓存去重, hashtable, intset
   5. 有序集合, ziplist或者跳跃表和hashtable

2. redis-cli key /span/del/

3. redis使用单线程模型,但是使用了I/O多路复用同时监听多个套接字实现了高效率
4. + 内存
   + I/O多路复用
   + 优化的数据结构和简单的操作
   + k-v的方式

5. redis事务是批量执行多组操作, 
   1. MULTI执行开始事务
   2. 将多个命令放入队列
   3. exec 开始执行,非原子性操作

6. 哨兵 

   + 监控主服务器和从服务器
   + 如果主服务器异常会让从服务器成为新的主服务器

   集群:

   redis分布式存储

7. + noXXXX: 不淘汰, 新的申请内存会报错
   + volatile 针对过期的数据集
     + LRU:最近最少使用淘汰
     + TTL: 最接近过期的淘汰
     + random: 随机淘汰
   + allkeys 所有集合
     + LRU:最近最少使用淘汰
     + random: 随机淘汰

8. rdb 快照, aof 日志

9. 全量复制: 刚开始是rdb快照,然后是日志增量执行

   部分复制: 通过复制偏移量获取数据缓冲区数据然后同步

10. + 缓存穿透, 请求不存在的key造成请求db压力过大, 过滤请求或者短时间缓存空数据

    + 击穿, 当热点缓存数据过期的时候, db压力过大,解决: 互斥锁, 随机睡
    + 雪崩, 大量的缓存同时过期,解决: 设置不同的过期时间

11. 跳跃表+ hashtable
12. + 设置缓存过期时间,自动过期更新
    + 先更新db再清除缓存
    + 通过服务将mysql的更新数据更新到redis数据库

13. setnx

    