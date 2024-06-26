
import math   # 메서드는 모듈.객체.메서드명()로 불러야 하지만, 함수는 모듈명.함수명()으로 바로 사용 가능

print(math.pi)
print(math.pow(5,2))   # 5의 2승


# 원의 넓이 : pi * r ^ 2 (^ = 컴퓨터에서 제곱을 표현함)

radius = 5
area = math.pi * math.pow(radius, 2)
print(f'반지름이 {radius}인 원의 넓이는 {area}입니다.')

# 로그계산

x = 2.718
log_value = math.log(x)
print('natural log: ',log_value)