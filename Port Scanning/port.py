import socket
import threading
from queue import Queue

# attacking localhost itself
target = '127.0.0.1'
queue  = Queue()
open_ports = []

# if a port is open, portscan will return true
def portscan(port):
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((target, port))
		return True
	except:
		return False
'''	
for port in range(1, 65365):
	result = portscan(port)
	if result:
		print("Port {} is open!".format(port))
		
#print(portscan(8001))
'''

def fill_queue(port_list):
	for port in port_list:
		queue.put(port)

# Complete all the ports scanning
def worker():
	while not queue.empty():
		port = queue.get()
		if portscan(port):
			print("Port {} is open!".format(port))
			open_ports.append(port)

# port_list is filled into queue
port_list = range(1, 65365)
fill_queue(port_list)

thread_list = []

# create 10 threads
for t in range(10):
	thread = threading.Thread(target=worker)
	thread_list.append(thread)
	
# start all threads
for thread in thread_list:
	thread.start()
	
# wait for all threads to finish
for thread in thread_list:
	thread.join()
	
print("Open ports are: ", open_ports)

