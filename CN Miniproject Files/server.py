import socket
import threading
import time

HOST="127.0.0.1"
PORT=8080
BUFFERSIZE=1024
CURR_CLIENT_NO = 0
TOT_CLIENT_NO=0
SERVER=None

connections=[]
addresses={}

def handle_client(client):
    


    client.close()
    

def accepting_client_connections():
    global CURR_CLIENT_NO
    global TOT_CLIENT_NO
    
    while CURR_CLIENT_NO<TOT_CLIENT_NO:
        CURR_CLIENT_NO+=1
        client,client_address=SERVER.accept()
        
        print("Connection "+str(CURR_CLIENT_NO)+" : "+client_address[0])
        client.send("Welcome to the quiz!".encode("utf-8"))

        addresses[client]=client_address
        client_handler_thr=threading.Thread(target=handle_client,args=(client,))
        client_handler_thr.start()


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