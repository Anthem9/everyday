import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)

    print("[*] Received: %s" % request)

    client_socket.send("ACK!")
    client_socket.close()

def main():
    bind_host = ''
    bind_port = 9999
    bind_address = (bind_host, bind_port)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(bind_address)

    server.listen(5)

    print("[*] Listening on %s:%d" % bind_address)

    while True:
        client, address = server.accept()

        print("[*] Accepted connection from: %s:%d" % (address[0],address[1]))

        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()