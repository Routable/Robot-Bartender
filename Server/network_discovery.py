import socket
import time
from logger import sys_log


def discover_clients():

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(0.2)
    broadcast_port = 37020

    message = b"application_password"

    sys_log("[network_discovery] starting search for clients on network.")

    while True:
        sys_log("[network_discovery] sending network broadcast on port %s" % broadcast_port)
        server.sendto(message, ('<broadcast>', broadcast_port))
        time.sleep(10)
