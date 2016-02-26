import threading
import socket
def accep():
    s = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 2222))
    s.listen(10)
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        print(data.decode('utf-8'))
        if data.decode('utf-8') == 'close':
            conn.close()
            break
        elif not data:
            break
        conn.send(data)
    pass
while True:
    threading.Thread(accep())
