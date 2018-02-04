import socket

server_host = "127.0.0.1"
server_port = 21567
server_address = (server_host, server_port)
buffer_size = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

while True:
    print("waiting for message...")
    data, address = server.recvfrom(buffer_size)
    server.sendto('%s'%data, address)
    print ("...received from and returned to:", address)

server.close()