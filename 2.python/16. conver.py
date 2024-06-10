# 1. 문자를 입력받아 대소문자를 변경하시오

# 소문자 -> 대문자 / 대문자 -> 소문자
# def convert():
#     x = input('pls enter: ')
    
#     if x.isupper():
#         lower = x.lower()
#         y = print(lower)

#     else:
#         upper = x.upper()
#         y = print(upper)
    
#     return y

# convert()

# 대문자는 소문자로, 소문자는 대문자로
def convert():
    str_list = []
    x = input('pls enter: ')   # my name IS Saemi 
    
    for i in x:
        if i.isupper():
            str_list.append(i.lower())

        elif i.islower():
            str_list.append(i.upper())

        else:
            str_list.append(i)
    return str_list   # ['M', 'Y', 'N', 'A', 'M', 'E', 'i', 's', 's', 'A', 'E', 'M', 'I']


def function_1():
    result = ''.join(convert())
    return print(result)

function_1()

# 소문자 및 대문자를 제외한 모든 것들을 그대로 출력하는 else 조건 / join 함수!!