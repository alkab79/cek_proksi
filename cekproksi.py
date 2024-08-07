import requests
from requests.auth import HTTPProxyAuth
import re

# Fungsi untuk memeriksa proxy
def check_proxy(proxy):
    # Tentukan apakah proxy adalah SOCKS atau HTTP/HTTPS
    if proxy.startswith('socks'):
        proxy_type = 'socks'
    else:
        proxy_type = 'http'

    proxies = {
        'http': proxy,
        'https': proxy,
    }

    try:
        print(f"Menguji proxy: {proxy}")  # Debugging line
        response = requests.get('https://www.google.com', proxies=proxies, timeout=5)
        if response.status_code == 200:
            return "Proxy aktif"
        else:
            return "Proxy tidak aktif"
    except requests.RequestException as e:
        print(f"Kesalahan saat menguji proxy {proxy}: {e}")  # Debugging line
        return "Proxy tidak aktif"

# Membaca proxy dari file
def read_proxies_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            proxies = [line.strip() for line in file if line.strip()]
        print(f"Daftar proxy dibaca dari {file_path}")  # Debugging line
        return proxies
    except FileNotFoundError:
        print(f"File {file_path} tidak ditemukan")
        return []
    except Exception as e:
        print(f"Kesalahan saat membaca file {file_path}: {e}")
        return []

# Menulis hasil ke file
def write_results_to_file(results, file_path):
    try:
        with open(file_path, 'w') as file:
            for proxy, status in results:
                file.write(f"Proxy {proxy} - {status}\n")
        print(f"Hasil ditulis ke {file_path}")  # Debugging line
    except Exception as e:
        print(f"Kesalahan saat menulis file {file_path}: {e}")

# Main
proxy_list = read_proxies_from_file('proxy_list.txt')

results = []
for proxy in proxy_list:
    status = check_proxy(proxy)
    results.append((proxy, status))

write_results_to_file(results, 'proxy_status.txt')
