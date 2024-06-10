# 차주 3일치 미션 : 랜덤 고객 데이터 생성기 > cvs 파일에 저장하기
import time

# WRITE
# with open('example.py', 'w') as write_file:
#     write_file.write('Hello, World. \n My name is Saemi. \t How are you?')
# print('Editing text done.')

# READ
# with open('example.py', 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line)
#         time.sleep(1)


import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', '20', 'Seoul'],
    ['Jane', '25', 'Busan'],
    ['Bob', '35', 'Jeju']
]

file_path = 'mydata.csv'

with open(file_path, 'a', newline='') as file:
    csv_writer = csv.writer(file)

    # csv_writer.writerow(['song', '32'])

    # for d in data:
    #     csv_writer.writerow(d)   # - 한줄 한줄 쓰기!

    csv_writer.writerows(data)   # - 한번에 쓰기

print('CSV 파일 작성 완료')


