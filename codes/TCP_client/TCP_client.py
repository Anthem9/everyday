import socket

target_host = 'www.baidu.com'
target_port = 80
target_address = (target_host, target_port)
buffer_size = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(target_address)

data = "GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n"
client.send(data)

response = client.recv(buffer_size)

print(response)