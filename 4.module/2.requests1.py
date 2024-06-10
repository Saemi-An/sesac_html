# 이전 파일은 파이썬 표준 라이브러리 / 이제는 외부 패키지를 내 pc에 설치

# requests : HTTP 요청을 할 수 있는 라이브러리
# pip install requests

import requests   # --> 리퀘스트 모듈 안에 있는 함수를 불러올 수 있음

response = requests.get('https://jsonplaceholder.typicode.com/users')   # 웹페이지에 있는 컨텐츠 가져오기

print('Web contents:', response)   # --> Web contents: <Response [200]> 
# < > 객체타입
print(response.status_code)
# print(response.text)

# text 결과물 받아온것을 json이라는 데이터 타입으로 변환
data = response.json()
# print('json data : ', data)

# userID = data['userID']
# title = data['title']
# print(f'사용자 아이디 : {userID}, 타이틀 : {title}')

users = data
for user in users:
    print('The first user: ', data[1])