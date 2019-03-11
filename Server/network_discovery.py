import socket
import time
from logger import sys_log


def discover_clients():

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(0.2)
    broadcast_port = 37020
    sleep_time = 3
    message = b"application_password"

    sys_log("Starting Client Sniffing (%ss intervals)  -  [network_discovery.py, discover_clients]" % sleep_time)

    while True:
        sys_log("Sending network broadcast on port %s  -  [network_discovery.py, discover_clients] " % broadcast_port)
        server.sendto(message, ('<broadcast>', broadcast_port))
        time.sleep(sleep_time)
