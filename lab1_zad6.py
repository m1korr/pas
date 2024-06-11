import socket
import sys


def connect_to_server():
    if len(sys.argv) != 3:
        print("Użycie: python program.py <adres serwera> <port>")
        return

    server_address = sys.argv[1]
    port = int(sys.argv[2])

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_address, port))
            print(f"Połączenie z {server_address}:{port} udane.")
    except Exception as e:
        print(f"Nie udało się połączyć z {server_address}:{port}. Błąd: {e}")


if __name__ == "__main__":
    connect_to_server()
