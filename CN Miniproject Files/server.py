import socket
import threading
import time

HOST=""
PORT=8080
BUFFERSIZE=1024
CURR_CLIENT_NO = 0
TOT_CLIENT_NO=0
SERVER=None

connections=[]
addresses=[]

def accepting_client_connections():
    global CURR_CLIENT_NO
    global TOT_CLIENT_NO
    
    while CURR_CLIENT_NO<TOT_CLIENT_NO:
        CURR_CLIENT_NO+=1
        connection,address=SERVER.accept()
        
        print("Connection "+str(CURR_CLIENT_NO)+" : "+address[0])
        connection.send("Welcome to the quiz!".encode("utf-8"))
        connection.close()


def Main():
    global SERVER
    global TOT_CLIENT_NO
    TOT_CLIENT_NO=int(input("Enter max number of players : "))
    
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((HOST,PORT))
    SERVER.listen(TOT_CLIENT_NO)
    
    accepting_client_connections()
    
if __name__ == '__main__':
    Main()