# 이진 탐색(binary_search)

def binary_search(list, target):
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid # 정답 찾음
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1

my_list = [5, 3, 8, 8, 12, 14, 15]
target = 8
result = binary_search(my_list, target)
if result != -1:
    print('targent index:', result)
else:
    print('target not found.')
