from socket import AF_INET, socket, SOCK_STREAM
from timeit import default_timer as timer
from threading import Thread
import sys, select, tkinter, time

start_time=0.0
sent = 0

def send_ans(ans):
	# end_time=timer()
	# time=end_time-start_time
	# print(time)
	# if time<=60:
	# 	client_socket.send(bytes(str(ans),"utf8"))
	# else:
	# 	client_socket.send(bytes(str("e"),"utf8"))
	# t_out = Thread(target=timeout).start()
	client_socket.send(bytes(str(ans),"utf8"))
	global sent
	sent = 1

def timeout():

	start_time = timer()
	global sent
	# print("tout cell")
	while(1):
		if (timer() - start_time > 60):
			client_socket.send(bytes(str("e"),"utf8"))
			client_socket.send(bytes(str(timer() - start_time),"utf8"))
			break
		else:
			if sent:
				# print("answer sent")
				client_socket.send(bytes(str(timer() - start_time),"utf8"))
				sent = 0
				return
			else:
				continue

def send_name(name):
	if(name!=''):
		client_socket.send(bytes(str(name),"utf8"))
		entry_field.destroy()
		send_button.destroy()

def quit_app ():
	exit(0)