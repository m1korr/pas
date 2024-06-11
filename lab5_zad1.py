import socket


def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        print(f"Połączono z serwerem {server_ip}:{server_port}")

        while True:
            number = input("Podaj liczbę: ")
            s.sendall(number.encode())
            response = s.recv(1024).decode()
            print(f"Odpowiedź serwera: {response}")
            if "odgadłeś" in response.lower():
                break


if __name__ == "__main__":
    main()
