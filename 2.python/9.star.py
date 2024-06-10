# *
# **
# ***
# row = int(input('Pls enter: '))
# for i in range(1,row+1):
#     print('*'*i)

#    *
#   **
#  ***
# ****
# row = 4
# star = 1, 2, 3, 4
# ' ' = 3,2,1,0
# rows = int(input('Pls enter: '))
# for i in range(1,rows+1):
#   print(' '*(rows-i),end='')
#   print('*'*i)


#   *
#  ***
# *****
# 행 = 3
# 별 = 1, 3, 5
# 공백 = 2, 1, 0
# rows = int(input('Pls enter: '))
# for i in range(1,rows+1):
#   print(' '*(rows-i),end='')
#   print('*'*(i*2-1))



*******
 *****
  ***
   *

row = 5
star = 9, 7, 5, 3, 1 => ()
' ' = 0, 1, 2, 3, => (i-1)

rows = int(input('Pls enter: '))
for i in range(1,rows+1):
    print(' '*(i-1))
    print('*'*())