from connection import Connection
from csv_writer import Csv_Writer


def main():
    connection = Connection(8888, 4)
    csv_writer = Csv_Writer('measurements.csv', ['time', 'orientation_x', 'orientation_y', 'orientation_z'])
    csv_writer._create_file_with_headers()
    while True:
        measurements = connection.get_measurements()
        csv_writer.add_line_of_data(measurements)


if __name__ == '__main__':
    main()
