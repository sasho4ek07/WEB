import socket
import threading

# Our thread class:
class ClientThread(threading.Thread):

    # Override Thread's __init__ method to accept the parameters needed:
    def __init__(self, conn, details):
        self.conn = conn
        self.details = details
        threading.Thread.__init__(self)

    def run(self):
            data = self.conn.recv(1024)
            msg = data.decode('utf-8')
            print(msg)
            if not data:
                conn.close()
            elif msg == "close":
                conn.close()
            else:
                self.conn.send(data)
                #print(conn)
                self.conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 2222))
server.listen(10)

# Have the server serve "forever":
while True:
    conn, details = server.accept()
    ClientThread(conn, details).start()
