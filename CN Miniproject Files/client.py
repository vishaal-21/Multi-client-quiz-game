import socket
import main
from threading import Thread
import time,sys,select
import tkinter
# import timer

HOST=""
global PORT
BUFFERSIZE=4096

HOST=input("Enter Host address : ")
PORT=int(input("Enter port number : "))

CLIENT = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
CLIENT.connect((HOST,PORT))

def start_game():
    print("hello")

main.initialize()
client_thread=Thread(target=start_game)
client_thread.start()
CLIENT.close()