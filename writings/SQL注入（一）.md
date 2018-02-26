# SQL注入（一）

结构化查询语言(Structured Query Language)简称SQL，是一种特殊目的的编程语言，**是一种数据库查询和程序设计语言**，用于存取数据以及查询、更新和管理关系数据库系统；同时也是数据库脚本文件的扩展名。

## MYSQL简介

•MySQL是一种关系数据库管理系统，**关系数据库将数据保存在不同的表中**，而不是将所有数据放在一个大仓库内，这样就增加了速度并提高了灵活性。

MySQL所使用的 SQL语言是用于访问数据库的最常用标准化语言

PS：是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据。现实世界中的各种实体以及实体之间的各种联系均用关系模型来表示。

## MYSQL数据库结构

数据库——表——列——字段

![](https://raw.githubusercontent.com/Anthem9/everyday/master/image/v2-c2839717b31fa1b2a3f456cf5505a733_hd.jpg)

![](https://github.com/Anthem9/everyday/raw/master/image/v2-be370f9b150a8f79551972913faf0754_hd.jpg)

![](https://github.com/Anthem9/everyday/raw/master/image/v2-e6511682fb94636ea32fbc24682e267d_hd.jpg)

## 数据库的查询

**SQL基本语句**

* Show databases;（显示所有数据库）

* Use xxx; (数据库名字)选择数据库

  use hack;

* Show tables;(显示所有表单)

* SELECT **列名称** FROM **表名称** WHERE **条件** #从表中选取数据

  Select \* from user where name= ‘bob’;

  PS:如果列名处是\*代表返回所有列

* 
  UPDATE **表名称** SET **列名称=新值** WHERE **条件** #修改表中某值

  update user set password=’654’ where name=’bob’

* insert into **表名称(字段名称)** values**（值1，值2，…….）**

  \#向表格中插入新的行，其中values中插入的值可为逻辑运算的结果

  eg.:insert into user(name,pass) values (’cindy’,’555’);

* delete from **（表）** where **条件**

  \#删除一个字段。

  Eg：delete form user where name=‘alex’

* union select 联合查询

  \#UNION 操作符用于合并两个或多个 SELECT 语句的结果集。

  请注意，UNION 内部的每个 SELECT 语句必须拥有相同数量的列。**列也必须拥有相似的数据类型。同时，每个 SELECT 语句中的列的顺序必须相同。**

  SELECT column_name(s) FROM table_name1

  UNION

  SELECT column_name(s) FROM table_name2

  Eg：

  SELECT message FROM messages

  UNION

  SELECT adminu FROM admin

* **杂七杂八**

  1）注释符：#， --+ ，//

  显而易见用于注释》。。。

  2）ORDER BY 语句用于对结果集进行排序,注入攻击中用于测试列的数量。

## SQL在PHP中的应用

一个基本的查询QQ号程序。

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-33a3d6e0655c948bcfba3f12a77ffe40_hd.jpg)

```
$query="select * from user where qq= '$qq'";
处为我们执行的查询语句。
由上面可知我们传入的QQ参数被放入此处执行，并且在MYSQL中执行了
select * from user where qq='xxxx'的操作。
进行SQL注入第一步就是要猜测后台使用的查询语句是什么样的。

```

## 什么是sql注入

* 攻击者通过构造恶意的SQL语句，使得数据库执行危险操作
* 比如本来是查询书籍的语句，结果显示了用户的密码
* 比如直接用数据库写入文件。

**SQL注入产生的原因**

简而言之，SQL注入产生的原因，就是我们使用了了一个可以被黑客控制并任意修改的SQL语句，使得黑客执行他所想进行的查询或者操作。

```
•$query="select * from user where qq='$qq'";
•
•这是我们的查询语句，$qq是我们的变量，本来这里是提交QQ号的。比如QQ=123456
•查询语句为： select * from user where qq=‘123456’

```

select * from user where qq=‘123456’
这已经是一个完整的语句了，可以显示结果了。但是我们先查看别的表单怎么办呢？我们并不能操作user的位置。这时我们就要再运行一个查询。

•可以发现select * from user where qq=‘123456’

•我们提交的东西都在单引号内部，都被作为参数了。我们想要再运行一个参数就要提前把单引号闭合，**这样我们后面的指令就不再是查询参数了。**

**PS：如何使得双引号闭合也是一门学问。**

```
假如我们查询的qq为12345‘ union select * from admin --+
这时语句为select * from user where qq=‘12345‘ union select * from admin --+’

```

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-7d10ebe37caa1c0401ec7228b3d54981_hd.jpg)

我们看看在实际运行的结果

![img](https://github.com/Anthem9/everyday/raw/master/image/v2-31976ccf06ad10c855ed82307dc2b607_hd.jpg)

结果多了一条信息，这是管理员的账号密码。

```
这是我们提交的QQ号
12345‘ union select * from admin --+

12345‘ 到这里为止正好和原查询语句一致

select * from admin 这里是我们自己定义的查询

Union 把后面我们查询的结果和前面查询的结果一起显示。
--+注释符，把后面的单引号注释掉，以免报错。

```

到此为止，我们就进行了一次完整的SQL注入操作，获取了管理员的账号和密码，我们再来回顾一下过程：

1、猜测开发者所使用语句：select * from user where qq= '$qq'

2、如何执行我们自己的查询语句：闭合单引号 +查询语句，绕过过滤执行查询。

3、如何使得我们查询的结果显示出来：group_concat(),盲注,报错注入.....