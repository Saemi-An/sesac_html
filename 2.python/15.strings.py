s = 'hello world'

# print(s)
# print(s.lower())
# print(s.upper())
# print(s.islower())
# print(s.isupper())
# print(s.capitalize())   # 전체 str에서 첫 글자만
# print(s.title()) # 모든 단어의 첫 글자

# s2 = ' hellow world     !!'
# print(s.strip())   # str 앞뒤의 공백을 제거한다. 중간의 공백은 제거하지 않는다.

s3 = 'apple, banana,cherry, orange'

s3_list = s3.split(',')
# print(s3_list)

def parse_input(input):
    s3_clean_list = []
    for i in s3_list:
        s3_clean_list.append(i.strip())

    return s3_clean_list

s4_list = parse_input(s3)

# list comprehension : 파이썬의 특징이자 장점 

s4_list = [fruit.strip() for fruit in s3.split(',')]

print(s4_list)

