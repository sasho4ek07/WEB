import threading
import socket
s = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
s.bind (('', 2222))
s.listen (11)
while True:
    threading._start_new_thread
    conn, addr = s.accept ()
    while True:
        data = conn.recv(1024)
        if data.decode ('utf-8') == 'close':
            conn.close ()
            break
        elif not data:
            break
        conn.send (data)
