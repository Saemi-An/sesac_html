# list comprehension 
# []
# [표현식 for 항목 in 반복 (조건문)]


# 1. 1 ~ 10
# nums = [i for i in range(1, 11)]
# 최종적으로 표현할 변수명(i) for 항목(i) in range()
# print(nums)

# 2. 위 리스트의 각 숫자의 제곱을 구하고 싶으면?
# squres = [x**2 for x in range(1, 11)]
# print(squres)

# 3. 1부터 20까지 짝수들로 이루어진 리스트
# even_numbers = [x for x in range(1, 21) if x % 2 == 0]
# print(even_numbers)

# odd_numbers = [x for x in range(1, 21) if x % 2 == 1]
# print(odd_numbers)


# 4. 문자열의 각 글자를 대문자로 바꾼 리스트를 생성하시오.
# word = 'hello'
# 원하는 결과 1 = ['h', 'e', ...]
# 원하는 결과 2 = ['H', 'E', ...]

# x = []
# for i in word:
#     x.append(i.upper())
# print(x)

# upper_letters = [i.upper() for i in word]
# # 변수명 = [표현식 for 항목 in 반복 (조건문)]
# print(upper_letters)

# upper_str = ''.join([i.upper() for i in word])
# print(upper_str)

# ================= 점심시간 숙제 ==================

# 문자열의 글자 수 세기
words = ['apple', 'banana', 'cherry', 'dragonfruit', 'egg']
# # words_length = []

# # for i in words:
# #     words_length.append(len(i))

# # print(words_length)

# words_length = [len(i) for i in words]
# print(words_length)


# 문자열 리스트에서 길이가 3 이하인 단어들만 선택하기 
# short_words = [i for i in words if len(i) <= 3]
# print(short_words)


# 중첩 리스트 펼치기 - [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nested_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # x = []
# # for i in nested_lst:
# #     for k in i:   # [1, 2, 3]
# #         x.append(k)
# # print(x)

# flattened_list = [k for i in nested_lst for k in i]
# print(flattened_list)


# 특정 조건(5보다 큰 것)을 만족하는 요소 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_5 = [i for i in numbers if i > 5]
print(greater_than_5)

# 문자열 리스트에서 첫 글자가 모음인 단어들 선택하기
words_2 = ['apple', 'banana', 'cherry', 'Apricot', 'egg']

vowel_starting_words = [i for i in words_2 if i.lower().startswith('a') or i.startswith('e') or i.startswith('i') or i.startswith('o') or i.startswith('u')]
print(vowel_starting_words)


