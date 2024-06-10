# raise : 내가 원하는 에러를 강제로 발생시키기

# def input_age(age):
    
#     if age < 0:
#         raise ValueError('Cannot take minus value')

#         print('Pls check your input.')
    
    
#     return age

def input_age(age):  
    try:
        input_age(10)
        input_age(-2)
    except ValueError as e:
        print('Please check your input.', e)
    
    return age

