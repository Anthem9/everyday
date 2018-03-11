# SS为Mac/Win设置系统全局代理

2017年5月12日

相信用过 Shadowsocks 的人都知道，在 MacOS 中 Shadowsocks 的全局模式只适用于浏览器 ( Windows 待验证)，其他 Application 是无法翻墙的，像终端、telegram 这些经常要用到翻墙的时候就有点烦。在这里安利 Proxifier 这个软件，用它就可以搞定这个需求了。
1、首先我们打开 SS 高级设置，可以看到 SS 的监听端口是1086：
![img](https://ooo.0o0.ooo/2017/05/12/59156a8e5d3c2.png)

2、下载 Proxifier，地址：<https://www.proxifier.com/mac/>

3、然后打开 Proxifier 应用，点击 Proxies，如图所示添加 127.0.0.1 1086 sock5
![img](https://ooo.0o0.ooo/2017/05/12/59156c1d394a1.png)

4、点击 Rules 编辑规则。
![img](https://ooo.0o0.ooo/2017/05/12/5915786292b13.png)

首先看到最后一个，Default 、Any、Any、Any、Proxy sock5 127.0.0.1:1086 ，这一行规则表明所有 ip 和端口都将走代理。**[这一条是必须要有的，这样所有应用就走代理了。]**

**显然我们有些应用是不希望走代理的，比如公司的本地ip、git、svn、QQ、微信、黄易云音乐等这些。。**

这个时候就需要添加排除规则了，**将 action 设置为 Direct，这样这个规则就是排除的规则**。你可以根据 application 名字，IP，端口来增加排除规则。[可以参考上图添加排除方案]。

从上图的 log 日志我们可以看到，由于我没有添加 Sogo 拼音的排除规则，所以他是默认走代理的，如果想要排除它，只需要添加 application 为 SogouServices，action 为 Direct 就可以了。