# 기능
# 1. 겜 > 저장? > 한 파일에 모두 저장 
# 2. 전체 히스토리 보기
# 3. 전체 히스토리에서 최소점수 소유자들 모두 출력

# 개선점
# 1. 게임 끝나면 자동저장 : 결국 파일에 {변수}를 저장해야함. 하지만 피클은 write만 있고 append는 없다. 히스토리 저장 및 열람을 피클로 할 수 있나?
# 2. txt 파일 저장시 \n 입력 없이도 애초에 한번에 한 줄씩 저장하는 함수?

import random
import datetime
import csv

class GAME:
    def __init__(self, name):
        self.name = name

    def Up_Down_Game(self):   # 게임실행 > 이번 게임 트라이 횟수 반환
        answer = random.randint(1, 100)
        print(answer)
        count_lst = ['1']
        for i in range(10):
            user_input = int(input('Pls enter(1 ~ 100): '))
            if user_input > answer:
                print('Down')
                count_lst.append('1')

            elif user_input < answer:
                print('Up')
                count_lst.append('1')

            elif user_input == answer:
                print('You won!')
                break
        now = datetime.datetime.today().strftime('%Y/%m/%d %H:%M')
        tries = str(len(count_lst))   # str
        info = [self.name, tries, now]

        f = open('test.csv', 'a')
        wr = csv.writer(f)
        wr.writerow(info)
        f.close()


f = open('test.csv', 'r')
rd = csv.reader(f)

lst = []
for line in rd:
    lst.append(line[1])
# print(lst)   # ['1', '1', '1', '1']

single_lst = []
for single in lst:
    single = int(single)
    single_lst.append(single)
print(single_lst)

min(single_lst)






        

        


