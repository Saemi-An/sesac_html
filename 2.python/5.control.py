# 제어문 : 반복문(for, while), 조건문(if)
# 키워드 : 언어에 정의되어 있는것. ex) del, while
print('while')
count = 0

while count < 10:   # while 조건이 True일 동안 / 아래 구문을 반복하라
    print(count)
    count = count + 2

print('')
print('for')
# for : 특정 목록 내에서의 반복

for i in range(5):
    print(i)

users = ['saemi','song','hyun','kim']

for i in users:
    print(i)

for num in [345,323,123]:
    print(num)

for i in range(1,10,2):   # 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(i)

for i in range(1,10,3):
    print(i)
