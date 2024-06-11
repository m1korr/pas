import socket
import random


def main():
    server_ip = "127.0.0.1"
    server_port = 12345
    secret_number = random.randint(1, 100)
    print(f"Wylosowana liczba: {secret_number}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((server_ip, server_port))
        s.listen(1)
        print(f"Serwer oczekuje na połączenia na porcie {server_port}...")

        conn, addr = s.accept()
        with conn:
            print(f"Połączono z {addr}")
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                try:
                    number = int(data)
                    if number < secret_number:
                        response = "Liczba jest większa."
                    elif number > secret_number:
                        response = "Liczba jest mniejsza."
                    else:
                        response = "Odgadłeś liczbę!"
                        conn.sendall(response.encode())
                        break
                except ValueError:
                    response = "Błąd: nieprawidłowa liczba."

                conn.sendall(response.encode())


if __name__ == "__main__":
    main()
