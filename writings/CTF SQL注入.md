# SQL注入

二 SQL注入Ctf中SQL注入基本上都是有过滤的，sqlmap基本上是不可能跑出来的，数据库基本上是mysql。

 ##（1）   部分关键词被过滤成空

1. 可能被过滤的是<  >  ”  ’ and from select等关键词。
2. ​
3. 如何判断哪些关键词被替换
4. ​
5. 比如?id=101，可以尝试?id=1<01，在101中间插入关键词<，如果页面仍然正确，则说明<被替换为空,可以利用<来绕过waf或者过滤。
6. ​
7. ？id=101 union select 1,2,3 from xxxx可以替换成？id=101 u<nion se<lect 1,2,3 fr<om xxxx
8. ​
9. 这样可以成功注入。

## （2）   大小写绕过

1. 比如select 可以写成SeLeCt

## （3）   双写绕过

1. 比如select 可以写成selselectect

## （4）   编码绕过

1. url，base64，hex编码等绕过

## （5）   mysql内联注释

1. 原语句：select *from user
2. ​
3. 改变后：/*!50001select*/ */*!50001from*/ user

## （6）   宽字节注入

1. 注入时，一般是引号’被转义成\’，这样就不能闭合前面的引号
2. ​
3. id=1’   会变成id=1\’
4. ​
5. payload:
6. id=1%df’,会变成id=1運’（ %df\'对应的编码就是%df%5c’，即汉字“運’），引号成功逃出。