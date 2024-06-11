import socket
import sys


def get_ip():
    if len(sys.argv) != 2:
        print("Użycie: python program.py <hostname>")
        return

    hostname = sys.argv[1]
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Adres IP dla {hostname} to {ip_address}.")
    except socket.gaierror:
        print(f"Nie udało się znaleźć adresu IP dla {hostname}.")


if __name__ == "__main__":
    get_ip()
