import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((host, port))
            print(f"[ОТКРЫТ] Порт {port} на {host}")
            return port
    except:
        return None

def scan_ports(host, ports):
    print(f"Сканирование хоста {host}...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = executor.map(lambda port: scan_port(host, port), ports)
        for port in results:
            if port:
                open_ports.append(port)

    if open_ports:
        print(f"Открытые порты на {host}: {open_ports}")
    else:
        print(f"Нет открытых портов на {host}")

if __name__ == "__main__":
    host = input("Введите IP-адрес или доменное имя: ")
    port_range = input("Введите диапазон портов (например, 1-1024): ")
    
    start_port, end_port = map(int, port_range.split('-'))
    ports = range(start_port, end_port + 1)
    
    scan_ports(host, ports)
