import socket, time, os

HOST, PORT = "127.0.0.1", 9000
SIZE = 5 * 1024 * 1024
DATA = b"x" * SIZE


def server():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(1)
    c, _ = s.accept()
    n = 0
    with c:
        while True:
            b = c.recv(65536)
            if not b:
                break
            n += len(b)
    print(f"server received {n} bytes")


def client():
    s = socket.socket()
    s.connect((HOST, PORT))
    t0 = time.time()
    s.sendall(DATA)
    s.close()
    print(f"client sent {SIZE} B in {time.time()-t0:.2f} s")


if __name__ == "__main__":
    import threading
    threading.Thread(target=server, daemon=True).start()
    time.sleep(0.2)
    client()