import socket
from threading import Thread
import time,sys,select
import tkinter
# import timer

HOST=""
global PORT
BUFFERSIZE=4096

HOST=input("Enter Host address : ")
PORT=int(input("Enter port number : "))

client_socket=socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))

def main():
    CLIENT = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    CLIENT.connect((HOST,PORT))
    
    data=CLIENT.recv(4096)
    print(data.decode())

    CLIENT.close()
    
if __name__ == "__main__":
    main()