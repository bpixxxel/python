import ssl
import socket

def verify_ssl_certificate(host, port=443):
    # Create a context for SSL
    context = ssl.create_default_context()

    # Connect to the host with SSL wrapping on the socket
    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            # Retrieve the certificate from the host
            certificate = ssock.getpeercert()

    # Check if the certificate is None
    if certificate:
        return certificate
    else:
        return "No certificate found or connection failed."

host = 'www.example.com'
certificate_info = verify_ssl_certificate(host)
print("Certificate Info for " + host + ":")
print(certificate_info)
