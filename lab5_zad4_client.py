import socket
import time


def measure_tcp_latency(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))
        start_time = time.time()
        s.sendall(b"ping")
        data = s.recv(1024)
        end_time = time.time()
        return end_time - start_time


def measure_udp_latency(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        start_time = time.time()
        s.sendto(b"ping", (server_ip, server_port))
        data, addr = s.recvfrom(1024)
        end_time = time.time()
        return end_time - start_time


def main():
    server_ip = "127.0.0.1"
    tcp_port = 12345
    udp_port = 12346

    tcp_time = measure_tcp_latency(server_ip, tcp_port)
    udp_time = measure_udp_latency(server_ip, udp_port)

    print(f"TCP latency: {tcp_time:.6f} seconds")
    print(f"UDP latency: {udp_time:.6f} seconds")


if __name__ == "__main__":
    main()
