fruit1 = '딸기'
fruit2 = '당근'
fruit3 = '수박'
fruit4 = '참외'
fruit5 = '메론'

fruits = ['딸기', '당근', '수박', '참외', '메론']
print(fruits)

print('')

complex_fruits = ['딸기', 'carrot', '123']
print(complex_fruits)

print('')

fruits_empty = []
print(fruits_empty)

print('')

for name in fruits:
    print(name)
    
print('')

for name in enumerate(fruits):
    print(name)
    
print('')

i = 0
while i < 5:
    print(fruits)
    i += 1
    
print('')

j = 0
while j < len(fruits):
    print(fruits[j])
    j += 1
