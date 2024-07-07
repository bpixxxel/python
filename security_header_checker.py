import requests

def check_security_headers(urls):
    headers_to_check = [
        'Content-Security-Policy', 
        'X-Frame-Options', 
        'X-XSS-Protection', 
        'Strict-Transport-Security', 
        'X-Content-Type-Options'
    ]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            print(f"\nChecking URL: {url}")
            headers = response.headers
            found_headers = {key: headers.get(key, 'Missing') for key in headers_to_check}
            
            for header, value in found_headers.items():
                if value == 'Missing':
                    print(f"  {header}: MISSING")
                else:
                    print(f"  {header}: {value}")
        
        except requests.RequestException as e:
            print(f"Failed to reach {url}. Error: {e}")

# List of URLs to check
urls_to_check = [
    'https://example.com',
    'https://yourwebsite.com'
]

check_security_headers(urls_to_check)
