import socket

def start_client():
    host = '127.0.0.1' 
    port = 4444

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        while True:
            message = input("Client: ")
            s.sendall(message.encode())
            data = s.recv(1024)
            print('Received from server:', data.decode())


start_client()
