import csv
import time
file_path = "mydata.csv"

with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)
        time.sleep(1)