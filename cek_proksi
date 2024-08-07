import requests

# Fungsi untuk memeriksa proxy
def check_proxy(proxy):
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    try:
        response = requests.get('https://www.google.com', proxies=proxies, timeout=5)
        if response.status_code == 200:
            return "Proxy aktif"
        else:
            return "Proxy tidak aktif"
    except requests.RequestException:
        return "Proxy tidak aktif"

# Membaca proxy dari file
def read_proxies_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if line.strip()]

# Main
proxy_list = read_proxies_from_file('proxy_list.txt')

for proxy in proxy_list:
    status = check_proxy(proxy)
    print(f"Proxy {proxy} - {status}")
