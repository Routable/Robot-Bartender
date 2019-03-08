import threading
from network_discovery import discover_clients
from logger import sys_log
from connection import Server

if __name__ == '__main__':

    sys_log("[Main - Bartender v0.1] Starting Network Services")
    discover_client_devices = threading.Thread(target=discover_clients)
    discover_client_devices.start()

    s = Server()
    sock = s.setup_server()

    while True:
        try:
            connection = s.setup_connection(sock)
            s.get_message(connection)
        except:
          break






