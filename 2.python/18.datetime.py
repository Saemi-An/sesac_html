
import datetime

# 현재시간 출력 : 모듈명.객체명.함수명()
# current = datetime.datetime.now()
# print(current)

# 내가 원하는 시간 생성
# my_time = datetime.datetime(2006, 5, 4, 23, 30)
# print(my_time)
# print(type(my_time))

import os

# current_dir = os.getcwd()
# print(f'현재 작업중인 디렉토리는 {current_dir} 입니다.')

new_dir = 'myostestfile'
# os.mkdir(new_dir)
# print(f'현재 디렉토리에 새로운 파일 {new_dir}을 만들었습니다.')

# os.rmdir(new_dir)
# print(f'{new_dir}을 삭제하였습니다.')

my_path = os.getenv("PATH")
print(f'나의 환경변수는 {my_path}입니다.')

command = 'dir'
os.systme(command)

os.chdir()

os.system(command)