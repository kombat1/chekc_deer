import socket
import time


sock = socket.socket()
sock.bind(('', 4040))
sock.listen(1)
while 1:
    conn, addr = sock.accept()

    log = open('log.lst','a')


    time.sleep(0)
    data = conn.recv(1024)
    log_data = " [User]: ",data.decode()," [IP] ",addr," [Time:] ",time.ctime(),"\n"
    for i in log_data:
        print(i)
        log.write(str(i))
    conn.send(b'')
