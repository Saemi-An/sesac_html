import random

surname = ['김', '박', '이', '장', '최']
middlename = ['영', '경', '혜', '승', '하']
lastname = ['희', '림', '연', '미', '경']

names = ['John', 'Jane', 'Michael', 'Emily']

def generate_name():
    name = random.choice(surname) + random.choice(middlename) + random.choice(lastname)
    return name

for _ in range(11):
    print(generate_name())