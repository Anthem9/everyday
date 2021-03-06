# 记Burp死活抓不到本地包的问题

**一、Burp Suite有时能抓到包,有时不能抓到包**

解决方法:

出现这种问题的原因就是代理没有设置成全局的,只是设置成了局部的。

打开IE浏览器，依次打开工具->Internet 属性->连接->局域网设置

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210154611749)

点击局域网可以看到代理服务器,在这里设置代理IP地址、端口号

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210154712407)

然后点击确定即完成浏览器代理。然后下载Proxifier这个软件，Proxifier 是一款功能非常强大的socks5客户端,可以让不支持通过代理服务器工作的网络程序能通过HTTPS或SOCKS代理或代理链。安装完成后打开proxifier

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210155138801)

选择配置文件->代理服务器---->新建一个代理服务器

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210155331634)

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210155615044)

然后点击确定，上图中看到有个验证，这里指的是是否需要帐户密码，如果你们公司设置了就可以勾选并设置，设置完成后我们通过配置文件->代理规则可以看到default的一项

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210161155982)

在这里我们可以选择我们设置的代理，然后ok，现在我们就可以轻松使用代理进行任何软件的上网了，但是还有些服务无法使用，这里我们可以选择配置文件->高级->服务与其他用户，然后勾选proxifier的其他目标下面两项并确定，至此我们就可以轻松使其他服务联网了

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210161020564)

然后就可以进行全局代理了，电脑上所以的请求从8080端口过的都会被拦截

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210161505828)

**二、Burp Suite不能拦截localhost,127.0.0.1**

在本地搭建好DVWA之后localhost,127.0.0.1死活不能拦截

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210161804932)

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210161859954)

我用的是火狐浏览器，谷歌的能拦截

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210162336518)

最后发现火狐浏览器中有个地方引起的

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210162659895)

去掉之后就可以了。

**三、Burp Suite不能拦截火狐浏览器**

看是否安装了AutoProxy代理插件有时装了代理插件的话Burp Suite会拦截不到,有次我就遇到了,Burp Suite怎么改都拦截不到火狐浏览器，最后把代理插件禁用下就行了。

![img](https://github.com/Anthem9/everyday/raw/master/writings/%E8%AE%B0Burp%E6%AD%BB%E6%B4%BB%E6%8A%93%E4%B8%8D%E5%88%B0%E6%9C%AC%E5%9C%B0%E5%8C%85%E7%9A%84%E9%97%AE%E9%A2%98/20170210220556861)