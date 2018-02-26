import socket

target_host = "127.0.0.1"
target_port = 21567
target_address = (target_host, target_port)
buffer_size = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"AAABBBCCC",target_address )

data, addr = client.recvfrom(buffer_size)

print(data)
print(addr)