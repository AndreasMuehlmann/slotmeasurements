import socket

HOST = "192.168.4.1"
PORT = 12345

buffer = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"y\n")
        data = s.recv(1024).decode('utf-8')
        buffer += data
        line = buffer[:buffer.find("\n")]
        buffer = buffer[buffer.find('\n') + 1:]
        print(f'recv: {line}')

