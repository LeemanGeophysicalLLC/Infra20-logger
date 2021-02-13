# Copyright (c) 2020 Leeman Geophysical LLC.
# Distributed under the terms of the MIT License.

"""Receive and log data from the Infra20 instrument."""

import serial

#
# ONLY CHANGE THESE PARAMETERS
#
serial_port = '/dev/ttyUSB0'
serial_baudrate = 9600


def determine_filename(date_time):
    """
    Determine the name to use for a logfile. Rounds to nearest 15 minutes.

    Format: yyyy_jjj_hh_mm.txt
    """
    minutes = [0, 15, 30, 45]
    minute_idx = date_time.minute // 15
    date_time = date_time.replace(minutes[minute_idx])
    return datetime.strftime(date_time, '%Y_%j_%H_%M.txt')


# Open the serial port
ser = serial.Serial(serial_port, serial_baudrate)

logfile_open = False

# Loop forever - get the data and write it to file
while True:
    data = ser.readline()
    data_time = datetime.utcnow()

    # If there isn't a log file open, lets open one with the current minute
    if not logfile_open:
        filename_open = determine_filename(datetime.utcnow())
        f = open(filename_open)

    # Determine what filename we should be writing to
    filename_to_write_to = determine_filename(data_time)

    # If that isn't the file we have open, close it and open the correct one
    if filename_open != filename_to_write_to:
        f.close()
        f = open(filename_to_write_to)
        filename_open = filename_to_write_to

    f.write(f'{data_time:%Y-%m-%dT%H:%M:%S.%f},{data}\n')
    