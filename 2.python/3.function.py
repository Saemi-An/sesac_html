a = 5
b = 3
c = 'hello'


def print_variable():
    print(a,type(a))
    print(b,type(b))
    print(c,type(c))

def print_operation():
    # print(a+c,type(a+c))   # Type Error
    print(c+c,type(a+b))
    print(c+c,type(c+c)) 

print_variable()
print_operation()
print('a')
print('b')