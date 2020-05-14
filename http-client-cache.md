# http 缓存

参考:https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching?hl=zh-cn

## 作用:  网络提取内容开销大，客户端直接缓存数据

## 问题：如何兼顾客户端缓存和快速更新

## 实现方式

### http header 

- ETag: 验证令牌,资源未发生变化时不会传送任何数据
- Cache-Control

	- 概览：定义其缓存策略,也就是如何缓存各个响应以及缓存多久
	- 详细配置

		- “no-cache”和“no-store”
		- “public”与 “private”
		- “max-age”

### 实际设计:

- HTML: 被标记为“no-cache”，这意味着浏览器在每次请求时都始终会重新验证文档，并在内容变化时提取最新版本
- JavaScript 可以设置较长的缓存，因为添加 了版本指纹可以随时更新。
- image:图像缓存时不包含版本或唯一指纹，并设置为 1 天后到期。

*XMind: ZEN - Trial Version*