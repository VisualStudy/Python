print("이것은 프린트다")
print("C언어와 달리 세미 콜론이 필수가 아니다")
print("print()는 자체적으로 \n을 포함하고 있다")
print("만약 이어 붙이기를 원한다면 end =을 이용하거나 콤마(,)나 + 더하기 연산자를 사용해야 한다. ")

raba = "rabarata istaferium"

print(raba[2:8:2][::-1])

raba.split()
print(raba)

raba_list = [1, 2, 3, 4], [5, 6, 7, 8]

for data in raba_list:
    for num in data:
        print(num)