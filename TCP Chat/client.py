import socket
import threading

host = '127.0.0.1'# localhost
port = 55554

nickname = input('Choose a nickname: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# receive function is to note response from server
def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if message == 'NICK':
				client.send(nickname.encode('ascii'))
			else:
				print(message)
		except:
			print("An Error Occured!")
			client.close()
			break

# Send data to server
def write():
	while True:
		message = f'{nickname}: {input("")}'
		client.send(message.encode('ascii'))
		
receive_thread = threading.Thread(target=receive)
receive_thread.start()

writer_thread = threading.Thread(target=write)
writer_thread.start()
