import socket
import threading

def udp_server(sock):
    for _ in range(3):
        data, addr = sock.recvfrom(1024)
        sock.sendto(b'ACK:' + data, addr)

def tcp_server(sock):
    conn, _ = sock.accept()
    total = 0
    with conn:
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                break
            total += len(chunk)
        print(f'TCP server received {total} bytes in order')


if __name__ == "__main__":
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp.bind(("127.0.0.1", 5004))

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.bind(("127.0.0.1", 443))
    tcp.listen(5)

    threading.Thread(target=udp_server, args=(udp,), daemon=True).start()
    threading.Thread(target=tcp_server, args=(tcp,), daemon=True).start()

    print("Servers up. UDP:5004  TCP:443")
    threading.Event().wait()