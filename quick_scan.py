import socket

def scan_host(ip, port_range):
    # Define the target IP and port range to scan
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for the socket operations
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    
    return open_ports

# Input the target IP and the range of ports to scan
target_ip = input("Enter target IP: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# Perform the scan
found_ports = scan_host(target_ip, (start_port, end_port))
if found_ports:
    print("Open Ports:", found_ports)
else:
    print("No open ports found.")
