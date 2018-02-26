# TCP_server

## 知识点

* socket库
* threading库
* 英语单词

## socket库

* bind_host变量是空白的，这是对bind()方法的标识，表示它可以使用任何可用的地址
* s.listen()

设置并启动TCP监听器，参数设置最大连接数

* s.accept()

被动接受TCP客户端连接，一直等待直到连接到达，返回一个套接字对象和地址元组

## threading库

使用threading.Thread类来创建一个新线程

```python
client_handler = threading.Thread(target=handle_client, args=(client,))
```

target传入一个函数，args传入函数所需的参数

```python
client_handler.start()
```

开始这个线程

## 英语单词

* backlog 积压，待办事物列表，在编程中一般指待办事物的最大容量，如在socket.listen（backlog）中，指最大连接数。
* thread 线程
* process 进程
* handle 处理
* args = argument 参数
* terminate 终止