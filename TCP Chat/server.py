import socket
import threading

host = '127.0.0.1'# localhost
port = 55554

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# send message to all clients
def broadcast(message):
	for client in clients:
		client.send(message)
		
# handle each client logic
def handle(client):
	while True:
		# only when client is active
		try:
			message = client.recv(1024)
			broadcast(message)
		except:
		# when client is off
			index = clients.index(client)
			clients.remove(client)
			client.close()
			nickname = nicknames[index]
			broadcast(f'{nickname} left the chat'.encode('ascii'))
			nicknames.remove(nickname)
			break
			
# accept a connection with NICK name.
def receive():
	print('Server Started!')
	while True:
		client, address = server.accept()
		print(f'Connected with {str(address)}')
		
		client.send('NICK'.encode('ascii'))
		nickname = client.recv(1024).decode('ascii')
		nicknames.append(nickname)
		clients.append(client)
		
		print(f'Nickname of the client is {nickname}!')
		client.send('Connected to the server'.encode('ascii'))
		broadcast(f'{nickname} joined the chat!'.encode('ascii'))

		thread = threading.Thread(target=handle, args=(client,))
		thread.start()
		
receive()
