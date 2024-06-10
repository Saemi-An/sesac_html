
def remove_duplicate(lst):
    unique_list =[]

    for i in lst:
        if i in unique_list:
            pass
        else:
            unique_list.append(i)

    return unique_list


def remove_duplicate_2(lst):   # if ~ else를 if 하나로 단축한 버전!
    unique_list =[]

    for i in lst:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list

def remove_duplicate_3(lst):   # 중복된 값들을 자동으로 탈락시켜주는 set 자료구조를 사용!
    return list(set(lst))

numbers = [1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 6, 5]

unique_numbers = remove_duplicate_2(numbers)

print('Original list: ', numbers)
print('Unique list: ', unique_numbers)