import requests
from requests.auth import HTTPProxyAuth

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
        response = requests.get('https://api.bigdatacloud.net', proxies=proxies, timeout=2)
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

# Menulis hasil ke file (hanya proxy yang aktif)
def write_results_to_file(results, file_path):
    try:
        with open(file_path, 'w') as file:
            for proxy, status in results:
                if status == "Proxy aktif":
                    file.write(f"Proxy {proxy} - {status}\n")
        print(f"Hasil ditulis ke {file_path}")  # Debugging line
    except Exception as e:
        print(f"Kesalahan saat menulis file {file_path}: {e}")

# Mengonversi proxy ke format yang diinginkan
def convert_proxy_format(proxy):
    if proxy.startswith('socks'):
        if 'socks5' in proxy:
            return f"socks5://{proxy.split('socks5://')[1]}"
        elif 'socks4' in proxy:
            return f"socks4://{proxy.split('socks4://')[1]}"
    else:
        return f"http://{proxy.split('http://')[1]}"

# Menulis hasil ke file lain dalam format yang diinginkan
def write_formatted_proxies_to_file(results, file_path):
    try:
        with open(file_path, 'w') as file:
            for proxy, status in results:
                if status == "Proxy aktif":
                    formatted_proxy = convert_proxy_format(proxy)
                    file.write(f"{formatted_proxy}\n")
        print(f"Hasil format proxy ditulis ke {file_path}")  # Debugging line
    except Exception as e:
        print(f"Kesalahan saat menulis file {file_path}: {e}")

# Main
proxy_list = read_proxies_from_file('proxy_list.txt')

results = []
for proxy in proxy_list:
    status = check_proxy(proxy)
    results.append((proxy, status))

# Hanya menyimpan proxy yang aktif
write_results_to_file(results, 'proxy_status.txt')

# Menulis proxy aktif dalam format yang diinginkan
write_formatted_proxies_to_file(results, 'formatted_proxy_list.txt')
