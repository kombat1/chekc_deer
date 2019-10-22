import socket
import getpass

sock = socket.socket()
sock.connect(("192.168.0.111",4040))
sock.send(getpass.getuser().encode())
sock.close()
