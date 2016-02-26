import socket
import threading

def accep():
    conn, addr = s.accept()
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
s.listen(100)
while True:
    #conn = sock
    #print(conn, sep='\n')
    #accep(conn)
    th1 = threading.Thread(accep())
    th2 = threading.Thread(accep())
