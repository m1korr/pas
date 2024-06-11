import socket
import threading
from datetime import datetime

def log_event(event):
    with open("server_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} - {event}\n")

def handle_client(client_socket, addr):
    log_event(f"Połączenie z {addr}")
    while True:
        message = client_socket.recv(1024)
        if not message:
            break
        client_socket.sendall(message)
    log_event(f"Rozłączono z {addr}")
    client_socket.close()

def main():
    server_ip = "127.0.0.1"
    server_port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((server_ip, server_port))
    server.listen(5)
    print(f"Serwer nasłuchuje na {server_ip}:{server_port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Połączono z {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    main()
