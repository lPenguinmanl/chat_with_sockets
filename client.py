import socket
import threading
import time

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client.connect(("localhost", 8000))

def get_mes():
    while True:
        print(client.recv(1024).decode("utf-8"))  


def send_mes():
    name = input("Input ur name")
    get_message_thread = threading.Thread(
        target=get_mes, 
    )
    get_message_thread.start()
    while True:
        mes = str(input(":::"))
        if mes != " ":
            client.send((f"[{name}]:"+mes).encode("utf-8"))

if __name__ == "__main__":
    send_mes()