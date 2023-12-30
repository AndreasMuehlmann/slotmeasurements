import socket


class Connection:
    def __init__(self, port, length_expected):
        self.port = port
        self.length_expected = length_expected

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', port))

    def get_measurements(self):
        data, addr = self.socket.recvfrom(1024)
        split_data_line = data.decode('utf-8').split(',')
        if (len(split_data_line) != self.length_expected):
            raise Exception(f"expected range {self.length_expected} got {len(split_data_line)}")
        return [float(data.strip()) for data in split_data_line]
