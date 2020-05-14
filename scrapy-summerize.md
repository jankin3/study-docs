#### UserAgentMiddleware
今天用轮换UA抓取数据发现一直失效，打印出来print(request.headers)   发现
```
{b'Accept': [b'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'], b'Accept-Language': [b'en'], b'User-Agent': [b'Scrapy/1.5.1 (+https://scrapy.org)']}
```
是scrapy的默认headers，然而我确实设置了自己的UserAgentMiddleware，
```
DOWNLOADER_MIDDLEWARES = {
    'xxx.middlewares.RotateipMiddleaware': 542,
    'xxx.middlewares.UserAgentMiddleware': 512,
}

···
request.headers.setdefault('User-Agent', ua)
```
详细对比之后发现可能是系统的UserAgentMiddleware 占用了自己的headers，而自己用的是setdefault，所以修改ua失效.
主要原因是之前设置的优先级比较高所以setdefault可以生效，优先级在系统默认的UserAgentMiddleware之后就失效了
解决方案：1. setdefault 换成request.headers['User-Agent'] = ua
2.提高自己的UserAgentMiddleware优先级（   系统 'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': 400,
）
