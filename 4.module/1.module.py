
# mission 1 : 랜덤넘버 1 ~ 100 
import random   # 객체 안의 함수를 불러오기 위함
# a = random.randint(1,100)
# print(a)

# mission 2 : 주사위 던지는 함수
# def roll_dice():
#     first = random.randint(1,6)
#     second = random.randint(1,6)

#     return print(f'({first},{second})')
        
# roll_dice()

# mission 3 : 리스트에서 랜덤으로 하나의 요소를 선택하기
# elements = ['strawberry', 'watermelon', 'blueberry', 'pineappel', 'pale', 'banana', 'kiwi', 'apple']

# choose_random_single = random.choice(elements)
# print(choose_random_single)

# choose_random_multiple = random.sample(elements, 3)
# print(choose_random_multiple)


# mission 4 : 랜덤으로 숫자 리스트 섞기
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def shuffle_shuffle(x):
#     random.shuffle(x)
#     return x

# print('Original lst : ', elements)
# print('Original nums : ', numbers)

# print('Shuffled lst : ', shuffle_shuffle(elements))
# print('Shuffled nums : ', shuffle_shuffle(numbers))   # shuffle()는 원본을 섞어버린다. 반환값이 없는 함수이다.


# mission 5 : 랜덤으로 문자열 생성 (영문 대문자 6자리)
import string

letter_set = string.ascii_letters

small_letter_set = list(letter_set[:26])   # str
# print(small_letter_set)

big_letter_set = list(letter_set[26:])   # str
# print(big_letter_set)

number_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
# print(number_set)

symbol_set = ['@', '*' '!', '#', '$', '-', '%', '&', '(', ')', '+']
# print(symbol_set)

password_set = small_letter_set + big_letter_set + number_set + symbol_set
# print(password_set)

# print(''.join(random.sample(big_letter_set, 10)))


# mission 6 : 랜덤 초이스에서 가중치를 고려한 랜덤  <-- 이게 뭔소리지???
# mission 7 : 랜덤 비밀번호 생성 (대문자 or 소문자, 숫자 포함 8자리)
# PW = ''.join(random.sample(password_set, 8))
# print(PW)

# mission 8 : 강력한 비밀번호 생성 (대문자, 소문자, 숫자를 각각 최소 1개 이상 포함하는 8자리의 강력한 비밀번호)
# print(random.sample(password_set, 8))   # 대/소/숫/특 중 랜덤 8 (최소 조건 없음, 중복 포함)

# 대문자 / 소문자 / 숫자 / 특수문자를 최소 1개씩 포함한 8자리의 비밀번호 생성, 중첩 없이
# 4자리만 랜덤

a = random.choice(big_letter_set)   # 'H' - str
b = random.choice(small_letter_set)   # ['t']
c = random.choice(number_set)    # ['1']
d = random.choice(symbol_set)   # ['+']

e = random.sample(password_set, 4)   # ['#', 'F', '&', 'h']
for i in e:
    if i == a or b or c or d:
        e.remove(i)
