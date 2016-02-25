import _thread
import socket
s = socket.socket (socket.AF_INET , socket.SOCK_STREAM)
s.bind (('', 2222))
s.listen (11)
def accep ():
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
_thread.start_new_thread(accep())
