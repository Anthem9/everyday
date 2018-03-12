##### 十六进制转换

还存在一种十六进制余字符串进行比较运算时的问题。例子如下：

```
"0x1e240"=="123456"		//true
"0x1e240"==123456		//true
"0x1e240"=="1e240"		//false

```

当其中的一个字符串是0x开头的时候，PHP会将此字符串解析成为十进制然后再进行比较，0x1240解析成为十进制就是123456，所以与int类型和string类型的123456比较都是相等。

## 2 bool 欺骗

当存在json_decode和unserialize的时候，部分结构会被解释成bool类型，也会造成欺骗。json_decode示例代码：

```
$json_str = '{"user":true,"pass":true}';
$data = json_decode($json_str,true);
if ($data['user'] == 'admin' && $data['pass']=='secirity')
{
    print_r('logined in as bool'."\n");
}

```

运行结果：

```
root@kali:/var/www# php /root/php/hash.php
logined in as bool

```

unserialize示例代码：

```
$unserialize_str = 'a:2:{s:4:"user";b:1;s:4:"pass";b:1;}';
$data_unserialize = unserialize($unserialize_str);
if ($data_unserialize['user'] == 'admin' && $data_unserialize['pass']=='secirity')
{
    print_r('logined in unserialize'."\n");
}

```

运行结果如下：

```
root@kali:/var/www# php /root/php/hash.php
logined in unserialize

```

## 4 PHP5.4.4 特殊情况

这个版本的php的一个修改导致两个数字型字符溢出导致比较相等

```
$ php -r 'var_dump("61529519452809720693702583126814" == "61529519452809720000000000000000");'
bool(true)

```