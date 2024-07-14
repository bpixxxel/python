import ssl
import socket
from datetime import datetime

def verify_ssl_certificate(host, port=443):
    # Create a context for SSL
    context = ssl.create_default_context()

    try:
        # Connect to the host with SSL wrapping on the socket
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Retrieve the certificate from the host
                certificate = ssock.getpeercert()

        # Check if the certificate is present and return parsed information
        if certificate:
            return parse_certificate(certificate)
        else:
            return "No certificate found."
    except ssl.SSLError as e:
        return f"SSL error occurred: {e}"
    except socket.error as e:
        return f"Socket error occurred: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def parse_certificate(cert):
    # Parse and format certificate details
    issuer = dict(x[0] for x in cert['issuer'])
    subject = dict(x[0] for x in cert['subject'])
    valid_from = datetime.strptime(cert['notBefore'], "%b %d %H:%M:%S %Y %Z")
    valid_to = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
    return {
        "Issuer": issuer,
        "Subject": subject,
        "Valid From": valid_from,
        "Valid To": valid_to,
        "Version": cert.get('version', 'Unknown'),
        "Serial Number": cert.get('serialNumber', 'Unknown')
    }

host = 'www.example.com'
certificate_info = verify_ssl_certificate(host)
print(f"Certificate Info for {host}:")
for key, value in certificate_info.items():
    print(f"{key}: {value}")
