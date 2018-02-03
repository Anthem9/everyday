# 在Markdown文档里插入本地图片

经常需要在md文档里添加图片，网络上的图片还好说，如果插入本地图片，在移动时总会遇到各种路径问题。

下面就介绍用github解决这个问题的方法。

1.在github新建一个仓库，用来存放图片，把图片上传上去。

![](https://github.com/Anthem9/everyday/raw/master/image/1166760-20170718132600505-1222512467.png)



2.复制

![](https://github.com/Anthem9/everyday/raw/master/image/1166760-20170718134225224-2045872593.png)

3.在网上找了资料，发现只要改路径的一个文件名就可以显示图片了。发现原来github和md文件关联的图片地址是有一定的格式的，其格式如下：

<https://github.com/>用户名/repository仓库名/raw/分支名master/图片文件夹名称/`***`.png or`***`.jpg

按照此格式github会自动解析这个语法，并把图片在md文件中正常显示出来。

![](https://github.com/Anthem9/everyday/raw/master/image/1166760-20170718135751740-936617110.png)



上面是从网上找到的方法，把修改后的网址输入浏览器果然能直接打开那张图片，想来是图片下载地址无疑，毕竟原地址打开后还是GitHub的界面，所以第二步直接在Download上右键复制链接地址即可。不必修改网址。