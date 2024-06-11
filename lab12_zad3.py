import socket
import threading
import random


def handle_client(client_socket, addr, number_to_guess):
    while True:
        message = client_socket.recv(1024)
        if not message:
            break

        try:
            guess = int(message.decode('utf-8'))
            if guess < number_to_guess:
                response = "Too low"
            elif guess > number_to_guess:
                response = "Too high"
            else:
                response = "Correct"
                client_socket.sendall(response.encode('utf-8'))
                break
        except ValueError:
            response = "Invalid input, please send a number"

        client_socket.sendall(response.encode('utf-8'))

    client_socket.close()


def main():
    server_ip = "127.0.0.1"
    server_port = 12345
    number_to_guess = random.randint(1, 100)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"Serwer nasłuchuje na {server_ip}:{server_port}, liczba do zgadnięcia: {number_to_guess}")

    while True:
        client_socket, addr = server.accept()
        print(f"Połączono z {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr, number_to_guess))
        client_handler.start()


if __name__ == "__main__":
    main()
