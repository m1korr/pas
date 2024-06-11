import socket
import sys


def scan_ports():
    if len(sys.argv) != 2:
        print("Użycie: python program.py <adres serwera>")
        return

    server_address = sys.argv[1]
    open_ports = []

    try:
        for port in range(1, 1025):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                result = s.connect_ex((server_address, port))
                if result == 0:
                    open_ports.append(port)

        print(f"Otwarty porty na {server_address}: {open_ports}")
    except Exception as e:
        print(f"Nie udało się zeskanować portów na {server_address}. Błąd: {e}")


if __name__ == "__main__":
    scan_ports()
