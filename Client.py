# Import socket module 
import socket 
import subprocess
import ipaddress
import time
from subprocess import Popen, PIPE


  
def Main(): 

    host = '192.169.0.15'
    port = 12345
 
    network = ipaddress.ip_network('192.168.0.0/25')
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.setdefaulttimeout(1000)


    for i in network.hosts():
        try:
            i=str(i)
            print("Attempting connection to", i)
            s.connect((i, port)) 

            # If connection is accepted on port, we've found our server.
            print(i, " is reachable. Canceling search of network.")
            break
  
        except Exception as e:
            print(e)
            print(i, " is not Reachable")
            continue


    while True: 
    
        message = input("Enter your drink order: ")     # Order to send
        s.send(message.encode('ascii'))                 # message sent to server 
  
        data = s.recv(1024)                             # message received from server 
  
        print('Received from the server :',             # print the received message 
               str(data.decode('ascii'))) 
  
        
        ans = input('\nDo you want to continue(y/n) :') # ask the client whether he wants to continue 
        if ans == 'y': 
            continue
        else: 
            break
    # close the connection 
    s.close() 
  
if __name__ == '__main__': 
    Main() 