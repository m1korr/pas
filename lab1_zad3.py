import ipaddress

def validate_ip():
    ip = input("Podaj adres IP: ")
    try:
        ipaddress.ip_address(ip)
        print(f"{ip} jest poprawnym adresem IP.")
    except ValueError:
        print(f"{ip} nie jest poprawnym adresem IP.")

if __name__ == "__main__":
    validate_ip()
