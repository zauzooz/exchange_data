import sys
import socket

# tao socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print("Error: %s" % (error))

PORT = 15000
HOST = socket.gethostname()

s.bind((HOST, PORT))

s.listen(5)

while (True):
    conn, addr = s.accept()

    while (True):
        # recieve
        print("%s from client" % (conn.recv(1024).decode("utf8")))

        # send
        data = '2'
        conn.sendall(bytes(data, "utf8"))
