## 使用购买的 SSL 证书流程
原文: https://docs.iredmail.org/use.a.bought.ssl.certificate-zh_CN.html#postfixdovecotapachenginx-ssl

#### 1. openssl 命令生成一个新的 SSL 证书
```bash
openssl req -new -newkey rsa:2048 -nodes -keyout server.key -out server.csr
```
该命令会生成两个文件：
server.key：密钥文件。可用于解密 SSL 证书。必须保护好这个文件。
server.csr：用于申请证书的前面请求文件。购买 SSL 证书时服务商需要此文件

#### 2. 购买证书
它会要求你上传 server.csr 文件或输入该文件的内容，然后就可以 获得签发的 SSL 证书了。
通常情况下， SSL 服务提供商将会给你两个文件：
server.crt 证书文件
server.ca-bundle 
注意:这里可能直接配置的话仍然会提示风险，可以将 server.crt 和 server.ca-bundle 的内容追加到一个新文件里，然后以这个 新文件作为 SSL 证书。注意：server.crt 的内容要在前面。
```bash
cat server.crt server.ca-bundle > server.chained.crt
```

#### 3. 服务器配置
nginx
```bash
server {
    listen 443;
    ...
    ssl on;
    ssl_certificate /etc/pki/tls/certs/server.crt;
    ssl_certificate_key /etc/pki/tls/private/server.key;
    ...
}
```


## 本地chrome开发使用https
本来使用openssl已经配置好了本地的证书，但是因为是本地的证书浏览器一直警告，firefox还好虽然抱怨但是还是让你前往，chrome个鬼直接警告高级选项里面的`依然前往`也没有了。
然后就我选择的本地导入ssl证书，然后手动信任，既可以打开了。

https://learnku.com/articles/19237