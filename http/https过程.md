https执行过程

简单版本:

1. 客户端向服务器发送sayHello请求
2. 服务器端发送自己的https证书返回给客户端验证
3. 客户端验证证书, 通过则发送随机数作为对称加密的公钥传给服务器端,未通过则警告提醒
4. 此后通过对称加密开始传输信息



详细版本

1. 客户端向服务器发送sayHello请求,以及附带随机数 random1

2. 服务器端发送自己的https证书以及附带随机数 random2返回给客户端验证

3. 客户端验证证书, 

   + 问题, 如何验证证书?

      + `数字签名`, 这里涉及到证书的签发(Signing)和认证(Verification)

        signing: 证书元信息(域名,公钥,过期时间等等), 先hash生成数字摘要,然后使用CA的私钥加密生成密文. 证书和密文一起组成了证书. 

        verification(逆过程): 解压得到两个文件,证书和密文, 将证书使用相同的hash方法生成摘要A, 然后使用CA的公钥解密密文得到摘要B, 比较A与B

      + 上面的过程涉及到了CA的公钥?哪里获得? 如何认证?

        证书一般是证书链的方式,也就是服务器证书上面一般还有两级证书.通过证书链一级一级的向上验证,最上级的root证书,一般操作系统或者浏览器会内置.只有路径中所有的证书都是受信的，整个验证的结果才是受信

   通过则生成pre-master secret然后通过刚才的服务器公钥加密发送到服务器, 未通过则警告提醒

4. 服务器获取数据之后使用私钥解密, 再根据pre-master secret 和random1 和random2 生成master secret作为对称加密的公钥

5. 然后再后续的交互中就使用session Key和MAC算法的秘钥对传输的内容进行加密和解密





参考：

https://blog.csdn.net/huzhenv5/article/details/104578198

https://www.runoob.com/w3cnote/https-ssl-intro.html

https://www.jianshu.com/p/b0b6b88fe9fe