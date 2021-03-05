import socket
import threading

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server.bind(("localhost", 8000))
server.listen()
users = []

def sendall(data, user):
    for i in users:
        if i != user:
            i.send(data)


def listen(user):
    data = user.recv(1024)
    sendall(data, user)
   
    
def start_server():
    while True:
        user, addr = server.accept()
        if user not in users:
            users.append(user)
        print(f"user :: {addr[0]} has been connected")
        listen_server = threading.Thread(
            target=listen, 
            args=((user,))
        )
        listen_server.start()


if __name__ == '__main__':
    start_server()


