
# def div(a, b):
#     try:
#         result = a / b
    
#     except ZeroDivisionError:
#         return 'Cannot devide with 0.' 
       
#     except TypeError:
#         return 'Wrong input value'
    
#     except Exception as error_code:
#         print('Error Code:', error_code)
#         return 'NaN'
    
#     else:
#         print('Great!')

#     finally:
#         print('Print anyway regardless of your failure / success')

#     return result


# print(div(5, 3))
# print(div(10, 0))
# print(div(15, 5))


# 문자.숫자를 받아서 숫자로 변환하기

def convert_to_interger(num_str):
    try:
        result = int(num_str)
    except ValueError:
        print('Pls input number.')
        return None

    return result

print(convert_to_interger('20'), type(convert_to_interger('20')))
print(convert_to_interger('100'), type(convert_to_interger('100')))
print(convert_to_interger('a'), type(convert_to_interger('a')))