# TCP三次握手四次挥手

## TCP三次握手

![TCP三次握手](https://github.com/Anthem9/everyday/raw/master/writings/TCP%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B/TCP三次握手.png)

## TCP四次挥手

![TCP四次挥手](https://github.com/Anthem9/everyday/raw/master/writings/TCP%E4%B8%89%E6%AC%A1%E6%8F%A1%E6%89%8B%E5%9B%9B%E6%AC%A1%E6%8C%A5%E6%89%8B/TCP四次挥手.png)

TCP/IP是全双工的，每个方向都必须单独进行关闭。

上图中1和3没有先后顺序，在2和3之间服务器仍可以向客户端发送数据，客户端此时只能接收数据，而不能发送数据。