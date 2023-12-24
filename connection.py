import socket
import time


class Connection:
    def __init__(self, host, port, length_expected):
        self.host = host
        self.port = port
        self.length_expected = length_expected
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

        self.buffer = ""

    def is_connected(self):
        return True

    def get_measurements(self):
        self.socket.sendall(b"y\n")
        data = self.socket.recv(1024).decode('utf-8')
        self.buffer += data
        new_line_index = self.buffer.find("\n")
        if (new_line_index == -1):
            return [0.0 for _ in range(self.length_expected)]
        data_line = self.buffer[:self.buffer.find("\n")]
        self.buffer = self.buffer[self.buffer.find('\n') + 1:]
        split_data_line = data_line.split(',')
        if (len(split_data_line) != self.length_expected):
            return [0.0 for _ in range(self.length_expected)]
        return [float(data.strip()) for data in split_data_line]
