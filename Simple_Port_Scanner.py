import socket

def port_scanner(host, ports):
    print(f"Scanning host: {host}")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            sock.close()
        except:
            pass


target = "127.0.0.1" 
ports_to_scan = [21, 22, 80, 443]  # FTP, SSH, HTTP, HTTPS
port_scanner(target, ports_to_scan)
