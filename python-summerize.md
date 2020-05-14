### python 笔记

 #### 数据库：
+ 存储字符串时的引号问题：
 调用pymysql.escape_string('向数据库插入的数据')


#### 数据结构真的很严格
对比 0 == '0' 不等，一定注意格式转换


#### 正则
re.sub("\,", '||', title, count=0, flags=re.I | re.U).split('||') 
re.split 为什么出现很多NO