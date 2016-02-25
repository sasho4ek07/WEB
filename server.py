import socket
s = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
s.bind (('', 2222))
s.listen (11)
sock, addr = s.accept()
while True:
	data = sock.recv(1024)        
        if data == 'close':
            break
        elif not data:
            break
        sock.send (data)
	sock.close ()		
