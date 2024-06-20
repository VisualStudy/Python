fruits = ['딸기', '당근', '수박', '참외', '메론']

print(fruits[:2])
print(fruits[2:])
print(fruits[1:3])
print(fruits[-1])
print(fruits[-2])
print(fruits[-2:])


#특별 슬라이싱 구문 (reverse)
print(fruits[::-2])
print(fruits[1:3][::-1])


for hello in fruits:
    print('hello', hello)
    
for hello in range(1, 11, 1):
    print('world!', hello)