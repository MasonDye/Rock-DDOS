# ROCK-DDOS

[**English**](README.md)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**中文简体**](README_ZH-CN.md)

This project provides a simplified multi-proxy server CC attack simulator for educational and research purposes. Please note that any form of DDoS attack is illegal, and you must adhere to legal and ethical standards.

## Features

- Supports CC, UDP, TCP, NTP, ARP flood attacks, with partial support for proxies (reflection servers)

- Simulates multi-IP CC flood attacks using HTTP or SOCKS proxies
- Supports reading proxy lists from files
- Supports dynamic proxy pool updates
- Concurrent request sending

## Installation

```bash
pip install requests
pip install scapy
```

If you are running on Windows, you need to install npcap or winpcap.

## Usage

1. **Edit Python Code**:
   
   - Modify the target server and other parameters, such as:
     ```python
     target_ip = "10.192.162.1"   # Replace with the target IP address
     target_port = 80  # Replace with the target port
     packet_size = 1024  # Size of each packet
     ```
2. **Run the Script**:
   
   - After modifying the `target_url`, `num_threads`, and `num_requests` variables in the code to set the target URL, number of threads, and number of requests, run the command:
     
     ```bash
     python cc_attack.py
     ```

## Notes

- Any form of DDoS attack is illegal, and you must adhere to legal and ethical standards.
- This project is for educational and research purposes only and should not be used for any illegal activities.

## Contributions

Pull Requests to improve this project are welcome.

## License

MIT License

```
Please note that this document is only to demonstrate the process of sending HTTP requests. Actual DDoS attacks require more complex tools and strategies to implement. Any form of DDoS attack is illegal, and you must adhere to legal and ethical standards.
```
