def accep():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 2222))
    s.listen(10)
    conn, addr = s.accept()
    while True:
            data = conn.recv(1024)
            msg = data.decode('utf-8')
            print(msg)
            if msg == "close":
                conn.close()
                break
            elif not data:
                conn.close()
                break
            else:
                conn.send(data)
    conn.close()
    return

while True:
    threading.Thread(name='th1', target=accep())
    threading.Thread(name='th2', target=accep())
    threading.Thread.start('th1')
    threading.Thread.start('th2')
