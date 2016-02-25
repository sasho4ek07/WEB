import thread
import socket
def accep ():
    s = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
    s.bind (('', 2222))
    s.listen (10)
    while True:
        conn, addr = s.accept ()
        while True:
            data = conn.recv(1024)
            if data.decode ('utf-8') == 'close':
                conn.close ()
                break
            elif not data:
                break
            conn.send (data)
thread.start_new_thread(accep())
