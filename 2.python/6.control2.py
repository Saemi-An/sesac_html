print('if문')
# x = int(input('Pls enter any single num: '))

# if x < 10:
#     print('Your num is smaller than 10')
# else:
#     print('Your num is bigger than 10')

print('if문과 formatiing')
# score = int(input('Pls enter : '))

# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'F'

# print('Score: {0}, Grade: {1}'.format(score,grade))   # foramt()

# print(f'Your score is {score}, grade is {grade}.')   # f-string

print('if문')
math = int(input('Pls enter you math score: '))
eng = int(input('Pls enter you eng score: '))

if math >= 90 and eng >= 90:
    print('Pass')
else:
    print('Fail')