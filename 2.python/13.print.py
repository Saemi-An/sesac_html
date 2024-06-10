print('Hello')

# f-string
x = '123'
print(f'hello {x}')

# format()
name = 'Saemi'
my_variable = 37
print('Hello, {}. I am {} years old.'.format(name,my_variable))

# 문자열 포멧팅에 순번 부여하기
plural = 'they'
print('Hello, {2}. I am {0} years old. How are {1}?'.format(name,my_variable,plural))

# 문자열 연결 연산자

print('Hello,',' ',end='')
print('World!')

print('I am',end='\t')
print('hangry')

# % 

print('Hello, %s.' % name)
print('Hello, %d.' % my_variable)
