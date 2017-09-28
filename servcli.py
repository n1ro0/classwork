import socket


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 50001))
    s.sendall(b'Hello')
    data = s.recv(1024)
print(data)