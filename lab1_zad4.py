import socket
import sys


def get_hostname():
    if len(sys.argv) != 2:
        print("Użycie: python program.py <adres IP>")
        return

    ip_address = sys.argv[1]
    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
        print(f"Nazwa hosta dla {ip_address} to {hostname}.")
    except socket.herror:
        print(f"Nie udało się znaleźć nazwy hosta dla {ip_address}.")


if __name__ == "__main__":
    get_hostname()
