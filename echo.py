import socket
import threading

def accep(conn):
    while True:
        #print(conn)
        data = conn.recv(1024)
        msg = data.decode('utf-8')
        print(msg)
        if not data:
            break
        elif msg == "close":
            conn.close()
            break
        else:
            conn.send(data)
        print(conn)
    conn.close()
    return
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
while True:
    s.listen(1)
    sock, addr = s.accept()
    conn = sock
    #print(conn, sep='\n')
    #accep(conn)
    threading.Thread(target=accep(conn), args=(conn))
    #threading.Thread(name='th2', target=accep())
