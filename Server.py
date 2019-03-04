import socket 
import threading 
from _thread import *

  
print_lock = threading.Lock() 
  
# thread fuction 
def threaded(c): 
    while True: 
  
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('') 
              
            # lock released on exit 
            print_lock.release() 
            break
  
        print('Received drink order for', str(data.decode('ascii')), '. Adding to order queue.') 
  
        message = "Client order received. Drink making in progress."
        c.send(message.encode('ascii'))    # send data back to client.
  
    # closing the connection
    c.close() 
  
  
def Main(): 
    host = "" 
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("Server started on port:", port) 
  
    # put the socket into listening mode 
    s.listen(5) 
    print("Waiting for client connection.") 
  
    # a forever loop until client wants to exit 
    while True: 
  
        # establish connection with client 
        c, addr = s.accept() 
  
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 