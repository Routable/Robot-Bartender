import threading
import _thread
from _thread import *
import time
import socket
import threading
import time

print_lock = threading.Lock()
soc = socket.socket()
h1 = socket.gethostname()
host = socket.gethostbyname(h1)
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

    
def discover_clients():
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
  server.settimeout(0.2)
  message = b"application_password"

  while True: 
    server.sendto(message, ('<broadcast>', 37020))
    print("--- Searching for client devices ---")
    time.sleep(10)

    
def incoming_connection():
  print("Listening for incoming connections")
  while True: 
    try:
      conn, addr = soc.accept()     
      print ("Incoming connection from",addr)

      print_lock.acquire() 
      print('Connected to :', addr[0], ':', addr[1]) 

      start_new_thread(threaded, (conn,)) 

    except e as Exception:
        print(e)
        print_lock.release() 
        continue
  soc.close() 



def Main(): 
  print("Server Started - Starting Device Discovery")
  t1 = threading.Thread(target=discover_clients)
  t2 = threading.Thread(target=incoming_connection)
  t1.start()
  t2.start()


if __name__ == '__main__': 
  Main() 