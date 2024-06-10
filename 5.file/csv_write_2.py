
import csv
import time

data = [
    {'Name':'Saemi', 'Age':28, 'City':'Seoul'},
    {'Name':'Song', 'Age':32, 'City':'Daejun'},
    {'Name':'Kim', 'Age':56, 'City':'Jeju'}
]

file_path = 'mydata.csv'

with open(file_path, 'w', newline='') as file:
    headers = data[0].keys()

    csv_writer = csv.DictWriter(file, fieldnames=headers)

    # To write header
    csv_writer.writeheader()

    # To write content
    csv_writer.writerow(data)

print('CSV 파일 작성 완료')