# Uncomment this to pass the first stage 
import socket   
def main():     
    print("Logs from yousr program will appear here!")      
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)     s
    server_socket.accept() 
if __name__ == "main":     
    main()