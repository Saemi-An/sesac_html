# 5! = 5 * 4 * 3 * 2 * 1

def factorial(n):
    result = 1

    for i in range(n,0,-1):
        result = result * i

    print(f'Factorial {n} is {result}.')
    

