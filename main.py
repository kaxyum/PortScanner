from concurrent.futures import ThreadPoolExecutor
from mcquery import mcquery
import socket
from art import *

timeout = 0.5
min_ports = 0
max_ports = 65535

successful_ports = []

def query_port(args):
    host, port = args
    try:
        with mcquery(host, port=port, timeout=timeout) as data:
            print(f"Port {port} - Success")
            successful_ports.append(port)
    except (socket.timeout, ConnectionRefusedError):
        pass
    except Exception as e:
        print(f"Error on port {port}: {e}\n")

tprint("Port Scanner");
ip = input("Enter an IP adress : ")
host = ip.strip()

with ThreadPoolExecutor(max_workers=200) as executor:
    executor.map(query_port, [(host, port) for port in range(min_ports, max_ports)])

print("Ports found :", successful_ports)
