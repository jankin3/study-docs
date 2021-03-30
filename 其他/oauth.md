# oauth

## oauth是什么？

### 一个开放标准，允许用户(无需提供将用户名和密码)让第三方应用访问该用户在某一网站上存储的私密的资源

## 原理：

参考：http://www.ruanyifeng.com/blog/2019/04/oauth-grant-types.html

### 提供一个token令牌

### token

- 特点：短期，可撤销，有范围
- 如何获取token

	- 方式

		- 授权码（authorization-code）

			- 特点：最常用最安全，适用于有后端的web项目
			- 实现：前端返回code，后端使用code请求token

		- 隐藏式（implicit）

			- 实现：直接请求token

		- 密码式（password）

			- 风险很大，直接告诉账号密码

		- 客户端凭证（client credentials）

			- 适用于没有前端的命令行应用，即在命令行下请求令牌

- 使用token

	- 一般在请求头添加"Authorization: Bearer ACCESS_TOKEN"

- 更新token

	- 一般会一起返回一个refresh_token，用于刷新token

## 应用

参考：google登录官方文档
https://developers.google.com/identity/protocols/OAuth2

### 三方登录

## 联系

### openId

### openId connect

*XMind: ZEN - Trial Version*