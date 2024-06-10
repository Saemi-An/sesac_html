# def hello():
#     print('hello1')
#     print('hello2')
#     print('hello3')

# hello()

# def numbers(num1):
#     result = num1 + 4
#     return result

# numbers(9)   #   아무 결과가 안나옴. 출력하라는 명령어가 없기 때문. 그냥 numbers() 함수에 인자값을 넣어줬을 뿐
# print(numbers(9))   # 출력하라는 명령을 입력해야만 나온다

# number1 = numbers(3)   # 아니면 변수로 numbers()함수에 인자값을 넣은 것을 바인딩한 후
# number2 = numbers(4)

# print(number1)
# print(number2)   # 변수를 출력하라는 명령이 있으면 또 출력이 가능.

# 미션1. 덧셈을 하는 함수를 작성하시오

# def add(a,b):
#     x = a+b
#     return x

# x = add(3,4)
# print(x)

# def add_2(num1, num2):
#     return num1, num2, num1+num2   # python은 여러개의 리턴을 갖을 수 있다 (특별)

# print(list(add_2(13,17)))   # tuple로 반환된다 / list로 감싸면 그렇게 반환 된다.

# mission 2. - / * / /

# def sub(num1,num2):
#     return num1 - num2

# print(sub(10,27))

# def mul(num1,num2):
#     return num1 * num2

# print(mul(13,7))

# def div(num1,num2):
#     return num1 / num2

# print(div(5,0))   # ZeroDivisionError --> 예외처리!!! 나중에 배움


def sum(a,b):
    return (a+b)/2

sum(3,4)