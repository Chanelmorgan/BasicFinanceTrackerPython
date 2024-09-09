# This is an example, have to get actual file from bank app and check the format

import csv

# Reading the file
MONTH = 'may'

file= f"hsbc_{MONTH}.csv"

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

# Setting up the google sheet access