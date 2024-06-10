import csv

f = open('test.csv', 'w', newline='')   # 파일을 쓰기 모드로 오픈

write = csv.writer(f)   # 선택된 파일에 무엇을 적겠다는 함수를 변수로 바인딩

write.writerow(['안녕하세요'])   # 적는다.한줄에_쓴다([리스트 형식으로 적을 내용])

write.writerow(['안새미 입니다.', '나이는 28살', '개발자 지망생 입니다.'])

f.close()   # 파일 닫기

