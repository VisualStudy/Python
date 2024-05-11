print('<구구단 출력기>')

num = int(input('원하는 단을 입력하시오 :  '))

for var in range(1, 10, 1):
   print(num)
   print('*')
   print(var)
   print('=')
   print(num * var)