### 概括

存放消息的存储服务，


### 作用

+ 解耦

+ 削峰填谷

+ 异步消息



### 消息传递模型

1. 点对点

   特点：

   1. 队列消息传递模型，
   2. 允许多个消费者和生产者
   3. 一条消息只允许一个消费者消费
   4. 消息需要消费者主动从队列中获取

2. 发布/订阅

   特点：

   1. topic消息传递模型
   2. 允许多个消费者和生产者
   3. 一条消息允许多个消费者消费
   4. 消息自动广播，发送给消费者

总结：主要区别是是否允许多个消费者消费同一条消息

3. 广播





### 问题

1. 如何设置消息传递模型？

2. 订阅模型下消息积压如何算数量？