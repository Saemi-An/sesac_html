# 선형탐색 (linear search) : 앞에서부터 순차적으로 찾기
import time
import random

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
        
    return -1   # 못 찾았을 때 -1 반환

def denerate_random_numbers(count):
    random_numbers = [random.randint(1, 10_000_000) for _ in range(count)]
    return random_numbers

my_list = [5, 3, 2, 6, 8, 9, 0]
my_list2 = denerate_random_numbers(50_000_000)
target = 9

start_time = time.time()
result = linear_search(my_list2, target)
end_time = time.time()

diff_time = end_time - start_time
print(f'It took {diff_time}s.')

if result != 1:
    print('Target found. Index: ', result)
else:
    print('Target does not exist.')

# =============