import socket

def handle_client(client_socket):
    buffer = b''  # Initialize a buffer to store incoming data

    while True:
        data = client_socket.recv(1024)  # Read data from the client
        if not data:
            break

        buffer += data  # Append new data to the buffer

        while b'\r\n' in buffer:  # Process each complete command
            # Split the buffer on RESP line terminator
            command, buffer = buffer.split(b'\r\n', 1)

            if command.upper() == b'PING':  # Check if the command is PING
                response = b"+PONG\r\n"
                client_socket.sendall(response)

    client_socket.close()

def main():
    print("Logs from your programs will appear here!")

    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    
    while True:
        client_socket, _ = server_socket.accept()
        handle_client(client_socket)

if __name__ == "__main__":
    main()
