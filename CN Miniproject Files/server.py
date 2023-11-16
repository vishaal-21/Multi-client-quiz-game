import socket
import threading
import time
import pandas

HOST="10.86.3.121"
PORT=8080
BUFFERSIZE=1024
CURR_CLIENT_NO = 0
TOT_CLIENT_NO=0
SERVER=None

connections=[]
addresses={}

df=pandas.read_excel("Questions.xlsx")

def select_questions(sheet_name,client):
    global df,questions
    
    df=pandas.read_excel("Questions.xlsx",sheet_name=sheet_name)
    # print(df)
    
    questions=df.sample(n=6)
    print(questions)
    
    for row in questions.itertuples(index=False):
        print(f"Question : {row.Question}")
        # client.send(bytes(str(row.Question),"utf8"))
        
        print(f"Option 1 : {row.Option_1}")
        # client.send(bytes(str(row.Option_1),"utf8"))
        
        print(f"Option 2 : {row.Option_2}")
        # client.send(bytes(str(row.Option_2),"utf8"))
        
        print(f"Option 3 : {row.Option_3}")
        # client.send(bytes(str(row.Option_3),"utf8"))
        
        print(f"Option 4 : {row.Option_4}")
        # client.send(bytes(str(row.Option_4),"utf8"))
        
        print(f"Answer : {row.Answer}")
        
        combined=f"{row.Question}|{row.Option_1}|{row.Option_2}|{row.Option_3}|{row.Option_4}|{row.Answer}"
        print(f"Combined :{combined}")
        client.send(bytes(combined,"utf8"))
        
        client.recv(1024).decode("utf8")
    

def credential_check(credentials):
    with open('Credentials.txt', 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            if line==credentials:
                return True
    return False

def handle_client(client):
    client.send(bytes("Welcome to the quiz!","utf8"))
    
    credentials=client.recv(1024).decode("utf8")
    print(credentials)
    
    if credential_check(credentials):
        client.send("1".encode("utf8"))
    else:
        client.send(bytes("0","utf8"))
        
    sheet_name=client.recv(1024).decode("utf8")
    print(sheet_name)
    
    select_questions(sheet_name,client)
    

def Main():
    global SERVER
    global TOT_CLIENT_NO,CURR_CLIENT_NO
    TOT_CLIENT_NO=int(input("Enter max number of players : "))
    
    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.bind((HOST,PORT))
    SERVER.listen(TOT_CLIENT_NO)
    
    while CURR_CLIENT_NO<TOT_CLIENT_NO:
        CURR_CLIENT_NO+=1
        client,client_address=SERVER.accept()
        
        print("Connection "+str(CURR_CLIENT_NO)+" : "+client_address[0])

        # addresses[client]=client_address
        client_handler_thr=threading.Thread(target=handle_client,args=(client,))
        client_handler_thr.start()
        # client.close()    
    SERVER.close()
    
if __name__ == '__main__':
    Main()