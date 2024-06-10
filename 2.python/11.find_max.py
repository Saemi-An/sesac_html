numbers = [3,7,56,4,1,3,5,8,9,0]

def find_max(numbers):
    max_num = numbers[0]

    for i in numbers:
        if i > max_num:
            max_num = i
    print(f'The biggest number is {}.')

find_max(numbers)
            