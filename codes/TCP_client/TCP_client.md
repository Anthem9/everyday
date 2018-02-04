# TCPclient

## 知识点

* 套接字简介
* 地址家族
* TCP简介
* socket库

## 套接字

套接字（socket）是计算机网络数据结构，它体现了“通信端点的概念”。在任何类型的通信开始前，网络应用程序必须创建套接字。可以将它们比作电话插孔，没有它们无法进行通信。

套接字最初是为同一主机上的应用程序所创建，使得主机上运行的一个程序（又名一个进程）与另一个运行的程序进行通信。这就是所谓的进程间通信（Inter Process Communication, IPC）

有两种类型的套接字：基于文件的和面向网络的。 

## 地址家族

包括Python在内的大多数受欢迎的平台都使用术语地址家族（address family）及其缩写AF；其他比较旧的系统可能会将地址家族表示成域（domain）或协议家族（protocol family），并使用其缩写PF而非AF。

AF_UNIX 代表地址家族：UNIX

AF_INET 代表地址家族：因特网（IPv4）

AF_INET6 （IPv6）

AF_NETLINK 支持Linux的特殊类型套接字

AF_TIPC 支持Linux的另一种特性的套接字

## TCP

### 简介

TCP（Transmission Control Protocol， 传输控制协议）是一种面向连接的，可靠的，基于IP的传输控制协议。

它的主要目的是为数据提供可靠的端到端传输。

TCP在RFC793中定义，在OSI模型中的第四层工作。

它能够处理数据的顺序和错误恢复，并且最终保证数据能够到达其应到达的地方。

### TCP端口

TCP端口就是为TCP协议通信提供服务的端口。所有TCP通信都会使用源端口和目的端口，而这些可以在每个TCP头中找到。

1~1023：是标准端口组（忽略掉被预留的0），特定服务会用到这些标准端口。

1024~65535：是临时端口组。

## socket库

要创建套接字，必须使用socket.socket()函数，它的一般语法如下

```python
socket.socket(socket_family, socket_type, protocol=0)
```

socket_family是前面所述的地址家族

socket_type是套接字类型

创建TCP套接字要使用SOCK_STREAM作为套接字类型

创建UDP套接字要使用SOCK_DGRAM作为套接字类型

### 套接字对象内置方法

s.connect()

接受一个元组（host，port）作为参数，主动发起TCP服务器连接

s.recv()

参数为缓冲区大小（单位是字节），接受TCP消息

s.send()

发送TCP消息

##英语单词

* buffer 缓冲区
* response 响应
* process 进程
* stream 流
* steam 蒸汽
* host 主机
* transmission 传输
* protocol 协议
* domain 域，域名
* client 客户，客户端
* server 服务器

