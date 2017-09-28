import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 50000))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print("connected", addr, conn)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)