import time

from connection import Connection
from csv_writer import Csv_Writer


def main():
    connection = Connection("192.168.4.1", 8888, 3)
    csv_writer = Csv_Writer('measurements.csv', ['time', 'orientation_x', 'orientation_y', 'orientation_z'])
    csv_writer._create_file_with_headers()
    while connection.is_connected():
        measurements = connection.get_measurements()
        csv_writer.add_line_of_data([time.time()] + measurements)
        time.sleep(0.01)


if __name__ == '__main__':
    main()
