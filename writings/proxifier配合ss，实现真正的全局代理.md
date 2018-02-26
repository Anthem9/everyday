# proxifier配合ss，实现真正的全局代理

由于ss使用的是sockets5代理，一般情况下只有浏览器支持，可以实现科学上网。但很多用户希望自己的应用软件，像outlook或游戏之类的软件也实现科学上网。这就需要proxifier的配合。
软件可以在官网下载，[https://www.proxifier.com/](https://link.jianshu.com/?t=https://www.proxifier.com/download.htm)
目前仅支持windows和mac os，不支持手机。
此软件为收费软件，这里提供两个注册码, 软件分为Standard Edition和Portable Edition版本，注册码不通用，注册用户名任意。
L6Z8A-XY2J4-BTZ3P-ZZ7DF-A2Q9C（Portable Edition）
5EZ8G-C3WL5-B56YG-SCXM9-6QZAP（Standard Edition）
P427L-9Y552-5433E-8DSR3-58Z68（MAC）

### 打开软件，首先配置代理服务器。

![img](https://github.com/Anthem9/everyday/raw/master/image/1481881-97e5b7cb8b401b3b.png)

proxifier配合ss，实现真正的全局代理

### 如下图，添加地址127.0.0.1，以及ss里配置的本地端口，默认为1080，选择socks version 5

*（有的服务器可能不是默认的1080，比如我自己的，请注意核对。）*

![img](https://github.com/Anthem9/everyday/raw/master/image/1481881-74cebb86e69a85b9.png)

proxifier配合ss，实现真正的全局代理

### 配置好后，点击测试，如果显示下图的绿色文字，则表示配置正确。

![img](https://github.com/Anthem9/everyday/raw/master/image/1481881-a78541aadd47e7ef.png)

proxifier配合ss，实现真正的全局代理

### 接下来就要添加规则，来确定哪些软件是走代理的，哪些不用

![img](https://github.com/Anthem9/everyday/raw/master/image/1481881-3f83012a25b0e54a.png)

proxifier配合ss，实现真正的全局代理

按如图所示的添加，这里有个default规则，如果default旁边的action里边选择的时proxy socks5…则本机所有软件都会走代理。一般default会选direct，然后把你需要走代理的软件选成proxy socks5…

![img](https://github.com/Anthem9/everyday/raw/master/image/1481881-321fa1e701911daa.png)

proxifier配合ss，实现真正的全局代理

### 最后在首页就能看到你各个软件的情况。

![img](https://github.com/Anthem9/everyday/raw/master/image/1481881-560ddaf1d778c39b.png)

proxifier配合ss，实现真正的全局代理