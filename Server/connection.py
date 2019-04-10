import socket
import select
import sqlite3
from logger import sys_log
from pumps import Bartender

class Server:
    def __init__(self):
        self.server_addr = '', 12345
                    
    # Create a socket with port and host bindings
    def setup_server(self, bartender):
        self.bartender = bartender
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(120)
        sys_log("Network Configuration Completed  -  [connection.py, setup_server]")
        try:
            s.bind(self.server_addr)
        except socket.error as msg:
            print(msg)
        return s

    def setup_connection(self, s):
        s.listen(5)     # Allows five connections at a time, however we only service one.
        sys_log("Listening for Client  -  [connection.py, setup_connection]")
        conn, addr = s.accept()
        return conn
        

    def get_message(self, conn):
        while True:
            data = conn.recv(1024)
            data = data.decode(encoding='utf-8')
            data.strip()

            sys_log("Received command: %s. [connection.py, get_message]" % data)

            if data == "receive_database": 
                sys_log("Sending Database  -  [connection.py, get_message]")
                self.send_file("database", conn)

            elif data == "quit":
                sys_log("Server Disconnecting")
                break
                
            elif data == "make_drink":
              try:
                sys_log("Recieved Drink Order  -  [connection.py, make_drink]")
                print(data)
                drink_msg = b"Send_Drink"
                received_message = (str(drink_msg)+"\n")
                conn.send(received_message.encode()) 
                sys_log("Awaiting Drink Selection  -  [connection.py, make_drink]")
                drink = conn.recv(1024)
                drink = drink.decode(encoding='utf-8')
                drink.strip()
                print(drink)
                sys_log("Client drink order placed  -  [connection.py, get_message]")
                self.bartender.make_drink(drink)
                sys_log("Drink Order Finished  -  [conenection.py, get_message]")
                conn.close()

              except Exception as e:
                print(e)
                

            elif data == "test 1":
                sys_log("Performing Pump Test (Consecutive)  -  [connection.py, get_message]")
                self.bartender.test_pumps_all(5)

            elif data == "test 2":
                sys_log("Performing Pump Test (Simultaneous)  -  [connection.py, get_message]")
                self.bartender.test_pumps(5)
            
            elif data == "prime_pumps":
              self.bartender.prime_pumps()
              
            elif data == "clean_pumps":
              self.bartender.clean_pumps()
			  
            elif data == ".":
              conn.close()

            else:
                print(data)
                sys_log("Invalid Command Received [connection.py, get_message]")

        conn.close()



    def send_file(self, filename, conn):
        with open("database.db", 'rb') as f:
            content = f.read()

        size = len(content)
        conn.sendall(size.to_bytes(4, byteorder='big'))
        buff = conn.recv(4)
        resp = int.from_bytes(buff, byteorder='big')

        if size == resp:
            sys_log("Connection Verified. Transferring Database.  -  [connection.py, send_file]")
            conn.sendall(content)
            f.close()
        else:
            sys_log("Connect Problem. Cancelling transfer.  -  [connection.py, send_file]")

     
