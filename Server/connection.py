import socket
import select
from logger import sys_log


class Server:
    def __init__(self):
        self.server_addr = '', 12345

    # Create a socket with port and host bindings
    def setup_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sys_log("Network Configuration Completed  -  [connection.py, setup_server]")
        try:
            s.bind(self.server_addr)
        except socket.error as msg:
            print(msg)
        return s

    def setup_connection(self, s):
        s.listen(5)     # Allows five connections at a time
        sys_log("Listening for Client  -  [connection.py, setup_connection]")
        conn, addr = s.accept()
        return conn

    def get_message(self, conn):
        data = conn.recv(1024)
        data = data.decode(encoding='utf-8')
        data.strip()
        sys_log("Database Request Received  -  [connection.py, get_message]")

        if data == "receive_database":
            sys_log("Sending Database  -  [connection.py, get_message]")
            self.send_file("database", conn)

        elif data == "QUIT":
            sys_log("Server Disconnecting")
            conn.close()

    def GET(self):
        reply = input("Reply: ")
        return reply

    def send_file(self, filename, conn):
        with open("database", 'rb') as f:
            content = f.read()

        size = len(content)
        conn.sendall(size.to_bytes(4, byteorder='big'))
        buff = conn.recv(4)
        resp = int.from_bytes(buff, byteorder='big')

        if size == resp:
            sys_log("Connection Verified. Transferring Database.  -  [connection.py, send_file]")
            conn.sendall(content)
        else:
            sys_log("Connect Problem. Cancelling transfer.  -  [connection.py, send_file]")
