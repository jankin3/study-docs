# mysql 锁机制

https://learnku.com/articles/28772#c812c1 锁机制

## 作用：解决并发访问

## 所处的处置：一般,表锁在mysql server层，行锁在索引层

## 锁分类

### 锁粒度

- 表锁
- 行锁

	- 实现方式：索引加锁

- 页锁

### 兼容性

- 写锁

	- for update. 比读锁有更高的优先级

- 读锁

	- lock in share mode, 普通select innodb不会有任何锁

### 锁模式

- 记录锁
- 间隙锁
- next-key锁
- 意向锁

	- 是一个标记锁，为了实现表锁和行锁不同的锁粒度

- 插入意向锁

*XMind: ZEN - Trial Version*