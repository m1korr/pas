import socket
import time

# TCP Server
def tcp_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", port))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f"TCP Server connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

# UDP Server
def udp_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(("127.0.0.1", port))
        print(f"UDP Server listening on port {port}")
        while True:
            data, addr = s.recvfrom(1024)
            if data:
                s.sendto(data, addr)

if __name__ == "__main__":
    from threading import Thread
    tcp_thread = Thread(target=tcp_server, args=(12345,))
    udp_thread = Thread(target=udp_server, args=(12346,))
    tcp_thread.start()
    udp_thread.start()
    tcp_thread.join()
    udp_thread.join()
