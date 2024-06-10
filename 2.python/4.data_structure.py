# 자료구조 : 변수에 데이터를 담는 형태. list, tuple, dict ..

a = 5
b = [1,2,3,4,5]

d = {}

print(a)
print(b)
# print(b[5]) IndexError : list index out of range
print(b[4])

print(len(b))

fruits = ['apple','grape','strawberry','banana','dragonfruit']

print(fruits[2],fruits[4])

x = [1,2,3,4,5]
x.remove(3)
print(x)

x.append(3)
print(x)

x.insert(3,7)   # insert(인덱스넘버,삽입할_데이터)
print(x)

# TUPLE - 변경이 불가능한 리스트, immutable
c = (1,2,3,4,5)
# c.remove(3)
print(c)

# DICT - {key:value}
user_1 = {
    'name':'Saemi-An',
    'age':28,
    'address':'Seoul'
}
print(user_1)
print(user_1['age'])

user_1['sexuality'] = 'hetero'   # 딕셔너리에 데이터 추가하는 방법 : dict[key] = value
print(user_1)

del user_1['sexuality']   # 딕셔너리에서 데이터 지우는 방법: del dict[key]
print(user_1)