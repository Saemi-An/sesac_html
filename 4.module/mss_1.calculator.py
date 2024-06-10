# 연산자를 받는다 : + / - / * / /
# 숫자 2개를 받는다
# 무한반복 받도록

class Calculator:
    def __init__(self, operator, num1, num2):
        self.operator = operator
        self.num1 = num1
        self.num2 = num2
        
    def plus_cal(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 + num2
    
    def minus_cal(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 - num2
    
    def multiple_cal(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 * num2
    
    def devide_cal(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return num1 / num2
    
    def init_cal(self):
    
        while True:
            
            try:
                operator = input('What do you want to do? (Plus : +, Minus : -, Multiple : *, Divide : /) ')
            except :
                
            a = int(input('Pls enter the first number: '))
            b = int(input('Pls enter the second number: '))
        
            if operator == '+':
                x = self.plus_cal(a, b)
                print(x)

            elif operator == '-':
                x = self.minus_cal(a, b)
                print(x)

            elif operator == '*':
                x = self.multiple_cal(a, b)
                print(x)

            elif operator == '/':
                x = self.devide_cal(a, b)
                print(x)

            else:
                print('Error')
                break

saemi = Calculator(None, None, None)
saemi.init_cal()


# 의도치 않은 값 넣어보기
# 1. 연산자에 문자('a')를 넣는 경우
# 2. deivde에서 0을 넣는 경우
