import threading
from network_discovery import discover_clients
from logger import sys_log
from connection import Server

if __name__ == '__main__':

    print("")
    sys_log("[Main - Bartender v0.2] Starting Network Services")

    # Thread started to send multicast UDP broadcasts on port 37020.
    # When the client discovers the message, it will attempt to connect
    # to our server via TCP on port 12345.

    discover_client_devices = threading.Thread(target=discover_clients)
    discover_client_devices.start()

    server = Server()
    sock = server.setup_server()

    while True:
        try:
            connection = server.setup_connection(sock)
            server.get_message(connection)
        except Exception as e:
            print(e)
            sys_log("Exception: there was a problem with the connection. "
                    "The application will now quit. - [app.py, main]")
            break






