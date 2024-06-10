import csv
import time

file_path = "mydata.csv"

with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(row['Name'])