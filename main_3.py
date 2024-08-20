import socket

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        # Parse the RESP (Redis Serialization Protocol) request
        command = data.split(b'\r\n')
        if len(command) >= 4 and command[2].upper() == b'PING':
            response = b"+PONG\r\n"
            client_socket.sendall(response)

    client_socket.close()

def main():
    print("Logs from your program will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    while True:
        client_socket, _ = server_socket.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    main()