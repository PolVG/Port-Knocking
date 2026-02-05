import socket
import time
import sys

if len(sys.argv) < 3:
    print("Usage: python knock.py <target_ip> <port1> <port2> ...")
    sys.exit(1)

target_ip = sys.argv[1]
ports = sys.argv[2:]

for port in ports:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((target_ip, int(port)))
        s.close()
        print(f"Knocked on port {port}")
    except:
        print(f"Knocked on port {port} (no response)")
    
    time.sleep(0.5)  
