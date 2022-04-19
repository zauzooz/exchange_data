import socket
from time import sleep

# tao socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: %s" % (error))

PORT = 15000
HOST = socket.gethostname()


# ket noi den server
s.connect((HOST, PORT))


while(True):
    data = '1'
    # send
    s.sendall(bytes(data, "utf8"))

    # recieve
    print("%s from client" % s.recv(1024).decode("utf8"))
    break
s.close()
