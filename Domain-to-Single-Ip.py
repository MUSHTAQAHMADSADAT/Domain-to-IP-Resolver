import socket

def domain_to_ip(domain):
    try:
        # Get all addresses associated with the domain
        addresses = socket.getaddrinfo(domain, None)
        ip_set = {result[4][0] for result in addresses}
        
        print(f"The IP addresses of {domain} are:")
        for ip in ip_set:
            print(ip)
    except socket.gaierror:
        print(f"Could not resolve the domain: {domain}")

if __name__ == "__main__":
    print("=======================================")
    print("Information System Security Directorate of Afghanistan")
    print("=======================================")
    domain = input("Enter the domain to convert to IP: ")
    domain_to_ip(domain)
