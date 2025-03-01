import socket

def domain_to_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"The IP address of {domain} is {ip}")
    except socket.gaierror:
        print(f"Could not resolve the domain: {domain}")

if __name__ == "__main__":
    print("=======================================")
    print("Information System Security Directorate of Afghanistan")
    print("=======================================")
    domain = input("Enter the domain to convert to IP: ")
    domain_to_ip(domain)
