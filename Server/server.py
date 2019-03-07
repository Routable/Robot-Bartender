import threading

from drinks import drink_list
from network_discovery import discover_clients
from connection import incoming_connection
from logger import sys_log


def Main():
    sys_log("[Main - Bartender v0.1] Starting Network Services")
    discover_client_devices = threading.Thread(target=discover_clients)
    listen_for_incoming_connections = threading.Thread(target=incoming_connection)

    discover_client_devices.start()
    listen_for_incoming_connections.start()


if __name__ == '__main__': 
    Main()
