from _thread import *
import socket
import threading
from logger import sys_log

print_lock = threading.Lock()
soc = socket.socket()
host = socket.gethostbyname(socket.gethostname())

port = 12345
soc.bind((host, port))
soc.listen(5)


def threaded(conn):
    while True:
        length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
        msg = conn.recv(length_of_message).decode("UTF-8")
        print(msg)
        print(length_of_message)

        message_to_send = "Drink order received from server.".encode("UTF-8")
        conn.send(len(message_to_send).to_bytes(2, byteorder='big'))
        conn.send(message_to_send)
        print_lock.release()
        break


def incoming_connection():
    sys_log("[connection] listening for incoming connections on port %s" % port)

    while True:
        try:
            conn, addr = soc.accept()
            sys_log("[connection] incoming connection from %s" % addr[0])
            print_lock.acquire()
            sys_log("[connection] successfully connected to %s via port %s" % (addr[0], addr[1]))
            start_new_thread(threaded, (conn,))
        except:
            sys_log("[connection] a problem has occurred with the incoming connection. Closing connection.")
            print_lock.release()
            continue
            soc.close()
