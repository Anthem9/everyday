# SQLmap使用笔记

## 参数使用

* -u “$URL”   自动进行扫描 默认为GET方式

* \#--date “POST数据”                       POST方式

* \#--cookie "cookie数据"                COOKIE方式

* —current-db 获取当前数据库

* —current-user 获取当前用户名

* —count 获取数据量 后面可跟-D -T -C 进行指定

* -D 数据库名 指定数据库

* -T 表名 指定表

* -C 列名 指定列

* —privileges 查看用户权限

* —dbs 列出所有数据库

* —tables 列出数据库库中所有表 -D 指定数据库

* —columns 列出表中所有列 -T -D

* —dump 输出某一项 -C -T -D 

* \#-d "mysql://用户名:密码@地址:端口(3306)/数据库名"

  需要pyMySQL

* —sql-shell 进行sql管理（好像不能回显数据，只能执行sql语句）

* \#—delay 秒数 延时几秒进行基于时间的盲注

* \#-safe-freq 进行基于时间的盲注        页面无变化，布尔无变化，从来不报错

* —os-cmd="net user" 执行操作系统命令

* —os-shell 创建操作系统shell

* —tamper="脚本名字"

* 本地上传

  在sqlmap目录下新建一个目录mst

  在mst下创建自己想要上传的文件

  —file-write "./mst/mst.txt"

  —file-dest "d:/www/1.html"

* -m url.txt(绝对路径) 批量检测注入漏洞

* 结合Burp Suite Option

  -l burp.log —batch -smart

  —batch 自动选择yes

  -smart 启发式快速判断，节约时间

* —level = (1,5) 选择要执行的测试水平等级，默认为1

  level 1 GET/POST

  level 2 HTTP Cookie

  level 3 User-Agent/referer

* —risk =(1,3) 选择执行测试的风险等级，默认为1

  risk 1 测试大部分的测试语句

  risk 2 会增加基于事件的测试语句

  risk 3 会增加or语句的SQL注入测试

* -v (0,6)  选择3显示payload

* —proxy=http://ip:port 可使用Burp进行代理抓包

* ​

## Tamper脚本

## 文件目录

doc/ ---->>>该文件夹包含了SQLmap 的具体使用说明，例如多种语言的简要说明、PDF版的详细说明、FAQ、作者信息等。 

extra/ --->>>这里包含了SQLmap的多种额外功能，例如发出声响（beep)、运行cmd、安全执行、shellcode等。 

lib/ --->>>这里包含了SQLmap的多种连接库，如五种注入类型请求的参数、提权操作等。 

plugins/ --->>>这里包含了各种数据库的信息和数据库通用事项。 

procs/ --->>>这里包含了mssqlserver、 mysql、Oracle和postgresql的触发程序 

shell/ --->>>这里包含了多种注入成功后的多种shell远程连接命令执行和管理数据库 

tamper/ --->>>这里包含了绕过脚本，例如编码绕过、注释绕过等。 

thirdparty/ --->>>这里包含了一些其他第三方的插件，例如优化、保持连接、颜色等。 

txt/ --->>>这里包含了一些字典，例如用户浏览器代理、表、列、关键词等。 

udf/ --->>>这里包含了用户自己定义的攻击载荷。 

waf/ --->>>>这里包含了一些多种常见的防火墙特征。可以直接使用--identify-waf来进行检测。 

xml/ --->>>这里包含了多种数据库的注入检测载荷、旗标信息以及其他信息。在这里可以看到进行注入的。