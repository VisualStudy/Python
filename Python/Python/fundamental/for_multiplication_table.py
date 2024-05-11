print('<구구단 출력기>')

num = int(input('원하는 단을 입력하시오 :  '))

for var in range(1, 10, 1):
   print(num, end = ' ') # end=''으로 print문 출력 이어 붙이기
   print('*', end = ' ')
   print(var, end = ' ')
   print('=', end = ' ')
   print(num * var)