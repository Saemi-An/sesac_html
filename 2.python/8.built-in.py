# 빌트인 함수 : 기본적으로 탑재된 함수
# 모듈을 통해 추가적인 것을 불러기

# while True:
#     a = input('Please enter: ')
#     print(a)

# mission.3 

num1 = int(input('Pls give me a single number: '))
num2 = int(input('Pls give me another number: '))

def add():
    return num1 + num2

x = add()
print(f'The result of {num1} plus {num2} is {x}.')   # f-string 쓰려면 num1과 num2를 밖으로 빼면 된다.




