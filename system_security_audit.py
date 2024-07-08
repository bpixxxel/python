import socket
import ssl
import subprocess
from emoji import emojize

def check_hostname():
    hostname = socket.gethostname()
    print(f"Hostname: {hostname} {emojize(':desktop_computer:')}")
    
def check_ip():
    ip_address = socket.gethostbyname(socket.gethostname())
    print(f"IP Address: {ip_address} {emojize(':globe_showing_Americas:')}")
    
def ssl_cert_check(host):
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.connect((host, 443))
            cert = s.getpeercert()
            ssl_expiry = ssl.cert_time_to_seconds(cert['notAfter'])
            if ssl_expiry > ssl.cert_time_to_seconds('Jul 8 00:00:00 2024 GMT'):
                print(f"SSL Certificate for {host} is valid {emojize(':white_check_mark:')}")
            else:
                print(f"SSL Certificate for {host} is expiring soon! {emojize(':warning:')}")
    except Exception as e:
        print(f"Failed to retrieve SSL Certificate for {host} {emojize(':cross_mark:')} Error: {e}")

def system_security_check():
    try:
        result = subprocess.run(['sudo', 'iptables', '-L'], capture_output=True, text=True)
        if result.returncode == 0 and "Chain" in result.stdout:
            print(f"Firewall is active {emojize(':shield:')}")
        else:
            print(f"Firewall is not active {emojize(':fire:')}")
    except Exception as e:
        print(f"Error checking firewall status: {e} {emojize(':cross_mark:')}")

if __name__ == "__main__":
    check_hostname()
    check_ip()
    ssl_cert_check('www.example.com')
    system_security_check()
