numbers = list(range(1, 1001))
count = 0

for number in numbers:
    if number % 13 == 0:
        count += 1
        
print(f"1~1000 13의 배수의 개수: {count}")