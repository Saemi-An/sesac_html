users = [
    {
        "name": "Alice",
        "age": 25,
        "location": "Seoul",
        "car": "BMW"
    },
    {
        "name": "Alice",
        "age": 40,
        "location": "Jeju",
        "car": "Honda"
    },
    {
        "name": "Bob",
        "age": 30,
        "location": "Busan",
        "car": "Mercedes"
    },
    {   
        "name": "Charlie",
        "age": 35,
        "location": "Daegu",
        "car": "Audi"
    },
]

# users_1 = users[0]
# users_2 = users[1]
# users_3 = users[2]


# def find_user(name):
#     # 입력받은 사용자 정보를 출력하시오

#     if x == users_1['name']:
#         print(users_1)
#     elif users_2['name']:
#         print(users_2)
#     elif users_3['name']:
#         print(users_3)
#     else:
#         print('Data not found.')

# find_user('Alice')
# def lookup_user(name): 
#     x = []
#     for u in users:
#         if u.get('name') == name:
#             y = x.add(u)
#             return y
        
        


# 소문자로 이름을 검색한다면 ?
# lookup_user('alice')
# def lookup_user(name): 
#     x = []
#     for u in users:
#         if u.get('name').lower() == name.lower():
#             y = x.add(u)
#             return y


# 동명이인 모두 출력 ?
# lookup_user('alice')
# 동명이인의 목록 반환해라
# result = []

# def lookup_user(name): 
#     for i in users:
#         if i.get('name').lower() == name.lower():
#             result.append(i)
            
#     return result

# lookup_user('alice')

# mission 1 : Fidn user with name & age
# def find_user_2(name, age):
#     for i in users:
#         if i.get('name').lower() == name.lower() and i.get('age') == age:
#             return print(i)
        
# find_user_2('bob',30)


# mission 2 : 
# find_user_2(30)
# def find_user_2(name, age):
    
#     try:
#         for i in users:
#             if i.get('name').lower() == name.lower() or i.get('age') == age:
#                 x = print(i)

#             if name != type(users['name']):
#                 name = age
#                 x = print(i)

#         return x
    
#     except TypeError:
#          if name != str:
#                 name = age
#                 print(i)
        
# find_user_2(30)





# find_user_2() --> 다 나오도록
# def find_user_2(name = str, age = int):
#     for i in users:
#         try:
#             if i.get('name').lower() == name.lower() or i.get('age') == age:
#                 return print(i)
            
#         except TypeError:
#             print('Error. Search keyword needed.')
#             print(users)
        
# find_user_2(30)


# def find_user_2(name=None, age=None):
#     if name is None and age is None:
#         return users

#     for i in users:
#         # name & age
#         if name is not None and age is not None:
#             if i['name'].lower() == name.lower() and i['age'] == age:
#                 return i
            
#         # name
#         if name is not None:
#             if i['name'].lower() == name.lower():
#                 return i

#         # age
#         if age is not None:
#             if i['age'] == age:
#                 return i
    
#     return None

# find_user_2(age = 30)


# def find_user_3(search):
#     result = []

#     for i in users:
        
#         # 4개 다 있다
#         if (search.get('name') is not None and search['name'] == i['name']) and \
#             (search.get('age') is not None and search['age'] == i['age']) and \
#             (search.get('location')  is not None and search['location'] == i['location']) and \
#             (search.get('car')  is not None and search['car'] == i['car']):
#                 result.append(i)
#                 return result

#         # 3개만 있다
#         elif (search.get('name') is not None and search['name'] == i['name']) and \
#             (search.get('age') is not None and search['age'] == i['age']) and \
#             (search.get('location') is not None and search['location'] == i['location']):
#                 result.append(i)
#                 return result
        
#         elif (search.get('age') is not None and search['age'] == i['age']) and \
#              (search.get('location')  is not None and search['location'] == i['location']) and \
#              (search.get('car')  is not None and search['car'] == i['car']):
#                 result.append(i)
#                 return result
        
#         elif (search.get('name') is not None and search['name'] == i['name']) and \
#             (search.get('location')  is not None and search['location'] == i['location']) and \
#             (search.get('car')  is not None and search['car'] == i['car']):
#                 result.append(i)
#                 return result
        
#         elif (search.get('name') is not None and search['name'] == i['name']) and \
#             (search.get('age') is not None and search['age'] == i['age']) and \
#             (search.get('car')  is not None and search['car'] == i['car']):
#                result.append(i)
#                return result

#         # 2개만 있다
#         elif (search.get('name') is not None and search['name'] == i['name']) and \
#             (search.get('age') is not None and search['age'] == i['age']):
#                 result.append(i)
#                 return result

#         elif (search.get('name') is not None and search['name'] == i['name']) and \
#             (search.get('location')  is not None and search['location'] == i['location']):
#                 result.append(i)
#                 return result

#         elif (search.get('name') is not None and search['name'] == i['name']) and \
#               (search.get('car')  is not None and search['car'] == i['car']):
#                 result.append(i)
#                 return result

#         elif (search.get('age') is not None and search['age'] == i['age']) and \
#             (search.get('location')  is not None and search['location'] == i['location']):
#                 result.append(i)
#                 return result

#         elif (search.get('age') is not None and search['age'] == i['age']) and \
#             (search.get('car')  is not None and search['car'] == i['car']):
#                 result.append(i)
#                 return result

#         elif (search.get('location')  is not None and search['location'] == i['location']) and \
#             (search.get('car')  is not None and search['car'] == i['car']):
#                 result.append(i)
#                 return result

#         # 1개만 있다
#         elif (search.get('name') is not None and search['name'] == i['name']):
#                 result.append(i)
#                 return result

#         elif (search.get('age') is not None and search['age'] == i['age']):
#                 result.append(i)
#                 return result

#         elif (search.get('location')  is not None and search['location'] == i['location']):
#                 result.append(i)
#                 return result

#         elif (search.get('car')  is not None and search['car'] == i['car']):
#                 result.append(i)
#                 return result



search_criteria_1 = {'name' : 'Bob'}
search_criteria_2 = {'name' : 'Alice', 'age' : 40}
search_criteria_3 = {'location' : 'Jeju', 'car' : 'bmw'}
search_criteria_4 = {''}

# x = find_user_3(search_criteria_1)
# y = find_user_3(search_criteria_2)
# z = find_user_3(search_criteria_3)

# print(y)


def find_user_4(serach):
    result = []

    for u in users:
        if match_criteria(u, search):
            result.append(u)

    return result

def match_criteria(user,criteria):
    for key, value in criteria.items():
        if key == 'age':
            if key['age'] == criteria['age']:
                