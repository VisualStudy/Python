#02-1 첫 코딩 실습 // 
print('Hello😄')



#02-2 //
print('친구야~ 안녕~~.')
print('선배님 안녕하세요.')
print('교수님 안녕하세요.')

print(3 + 5)
print(17 * 234)
print(30 * 4 / 5)



#02-3 //
print('To do list : 2024 - 03 - 15')
print('1. 친구와 점심 식사')
print('2. 영어 회화 공부')
print('3. 영어 발음 훈련')
print('4. C언어 공부')
print('5. 파이썬 정리')
print('6. 잔디 심기')
print('7. 친구들과 채팅')



#03-1 //
myName='박지호'
myMajor='컴퓨터공학과'
myName='Jiho_Park'

print(myName)
print(myMajor)



#03-2 //
intro='Hello'
print(intro)



intro='안녕하세요'
print(intro)


#03-3 //
var = 10
print(var)
var = 'Hello Python'
print(var)



#03-4 //
add='Good morning!★Δ'
print(add)
print(add)
print(add)



#04-1 //
var1 = 777
var2 = '777'
var3 = 3.14

var1 = var1 + 1

print(var1)
print(var2)
print(var3)

flag = True
print(flag)

print('--------------------')

print(type(var1))
print(type(var2))
print(type(var3))
print(type(flag))

var2 = int(var2)
print(var2 + 1)
print(type(var2))

var4=''
print(type(var4))
var4 = bool(var4)
print(var4)

#04-2 //
print('Hello Python!')
print('Hello Python!')
print('Hello Python!')
print('Hello Python!')
print('Hello Python!')

print('---------------------------')

i = 'Hello 컴퓨터공학과 20240291 박지호'
print(i)
print(i)
print(i)
print(i)
print(i)

#05-1 //
print('[데이터 입력]')
userData = int(input('정수를 입력하세요 : '))

#userData = int(userData)

print(userData + 2)

print(type(userData))

#05-2 //
userData = int(input('숫자 입력: '))

print(userData + 1)

#05-3 //
userName = input('이름을 입력하세요: ')

print('사용자 이름')
print(userName)

userAge = input('나이를 입력하세요: ')

print('사용자 나이')
print('나이: ' + userAge + '살')

#05-4 //
print('회원 정보를 입력하세요')
userName = input('이름 : ')
userMail = input('메일 : ')
userId = input('아이디 : ')
userPw = input('비밀번호 : ')

            
print('-------------------------------------------------------------------')
print('To.  ' + userMail)
print('▶ 아이디 및 비밀번호 확인')
print(userName + ' 고객님 안녕하세요.')
print(userName + ' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
print('아이디 :  ' + userId)
print('비밀번호 :  ' + userPw)
print('-------------------------------------------------------------------')

#06-1 //
sales1 = int(input('1월 매출 : '))
sales2 = int(input('2월 매출 : '))
sales3 = int(input('3월 매출 : '))
total = sales1 + sales2 + sales3
print('1분기 전체 매출 : '+ str(total)+'원')

#06-2 //
sales = int(input('1분기 매출 : '))
purchase = int(input('1분기 매입 : '))
profit = sales - purchase
print('수익 : ',profit,'원')

#06-3 //
print('-'*30)

width = int(input('가로 길이 : '))
length = int(input('세로 길이 : '))

area = width * length

print('넓이 :', area,'㎠')

print('-'*30)

#06-4 //
weight = float(input('몸무게(kg) : '))
height = float(input('신장(m) : '))
bmi = weight / height**2
print('BMI :',bmi)


#07-1 //
myMoney = 5000000
rate = 0.05

myMoney += myMoney * rate
myMoney += myMoney * rate
myMoney += myMoney * rate
myMoney += myMoney * rate
myMoney += myMoney * rate

print('5년 후 총 수령액 : ', int(myMoney), '원')



#07-2 //
height = int(input('어린이의 신장을 입력하세요: '))

str = '탑승 가능' if height >= 120 and height < 170 else '탑승 불가능'

print(str)



#07-3 //
incoming = int(input('수입 : '))

outgoing = int(input('지출 : '))

result = '흑자' if incoming > outgoing else '적자'

print(result)


#08-1 //
carSpeed = int(input('자동차의 현재 속도는 : '))

if carSpeed >= 50:
    print('속도 위반!!')
    
#08-2 //
num = int(input('숫자를 입력하세요: '))

if num > 10:
    print('num은 10보다 크다.')

print('num:', num)


#08-3 //
score = int(input('점수를 입력하세요: '))

if score >= 80:
    print('합격입니다.')
else:
    print('아쉽습니다. 다시 도전해주세요.')

#08-4 //
temp = int(input('기계 온도를 입력하세요: '))

if temp >= 40:
    print('팬(Fan)가동')
    print('기계 온도가 40도 이상입니다.')
else:
    print('팬(Fan)중지')
    print('기계 온도가 40도 미만입니다.')

#09-1 //
mileage = 1200

if mileage >= 1000:
    print('마일리지 사용가능')
else:
    print('마일리지 사용불가')

#09-2 //
score = int(input('점수를 입력하세요.  '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
    
#09-3 //   
peopleNumber = int(input('인원수를 입력하세요. '))

if peopleNumber == 1:
    print('400,000원 지원')
elif peopleNumber == 2:
    print('600,000원 지원')
elif peopleNumber == 3:
    print('800,000원 지원')
else:
    print('1,000,000원 지원')

#09-4 //
num = int(input('양의 정수를 입력하세요.  '))

if num > 0: 
    print('num :', num)
    if num % 2 == 0:
        print('num은 짝수')
    else:
        print('num은 홀수')

else:
    print('양의 정수가 아닙니다.')
    if num == 0:
        print('num은 0입니다.')
    else:
        print('num은 음의 정수입니다.')
    
#09-5 //
print('1.월~금, 2.토요일, 3. 공휴일')

dayWeek = int(input('요일을 선택하세요. '))

if dayWeek == 1:
    print('버스 전용차로 단속 중입니다.')
    print('1.버스, 2.승용차')

    carType = int(input('차종을 선택하세요. '))

    if carType != 1:
        print('버스 전용차로 위반!!')
    else:
        print('버스입니다.')
        
else:
    print('토요일 및 공휴일은 단속하지 않습니다.')

#10-1 //
for i in range(1, 11, 1):
    print('안녕하세요.')
    print(i)
print('-----------------------------')

for num in range(2, 10, 2):
    print('num = ',num)
print('-----------------------------')

num = int(input('메일 발송 횟수를 입력하세요.'))

for num in range(1, num + 1, 1):
    print('메일발송!')
print('-----------------------------')

for num in range(1, 11, 1):
    print('num =', num)

    if num % 3 == 0:
        print('3의 배수!')
print('-----------------------------')

for num in range(1, 50, 1):
    print('num =', num)

    if num % 7 == 0:
        print('7의 배수!')

#10-2 //
sum = 0

for num in range(1, 11, 1):
    sum = sum + num

print('sum = ', sum)

print('----------------------------')

for i in range(10, 0, -1):
    print(i)

print('----------------------------')

for c in 'hello':
    print(c)

#10-3 //
n1 = int(input('출력하고 싶은 단을 입력하시오.'))

for n2 in range(1, 10, 1):
    print(n1, end = '')
    print('*', end = '')
    print(n2, end = '')
    print('=', end = '')
    print(n1 * n2)

#11-1 //
for num in range(1, 6):
    print(num)
else:
    print('반복이 끝났습니다!')
print('-------------------------')

for num in range(1, 11):
    if num % 2 == 0:
        continue
        print('짝수')
    print(num)
print('-------------------------')

num1 = 8
for num1 in range(1, 6):
    for num2 in range(num1):
        print('*', end = '')
    print()

#11-2 //
n1 = 9
for n1 in range(2, 10):
    for n2 in range(1, 10):
        print(n1, end = ' ')
        print('*', end = ' ')
        print(n2, end = ' ')
        print('=', end = ' ')
        print(n1 * n2)
    print()    

#11-3 //
num = 1

while num <= 10:
    print('num : ', num)
    num = num + 1

print('-----------------')
num = 1
while num <= 30:
    if num % 2 == 0:
        print('짝수:',num)
    else:
        print('홀수:', num)

    num = num + 1

#11-4 // 
num = 1

while num <= 9:
    print(3, '*', num, '=', 3 * num) 
    num += 1
print('--------------------------------------------')
num = 1
sum = 0

while num <= 10:
    sum = sum + num
    if sum >= 30:
        print('num : ', num)
        break
    num = num + 1
print('합계:', sum)

#12-1 // 
fruits = [ '사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나']
print(fruits)

member = []
print(member)


print(fruits[2])

print(len(fruits))

print(len('python'))


print('----------------------------------')


message = input('메시지를 입력하세요.')
print(len(message))

#12-2 //
balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']

for item in balls:
    print('item: ', item)


print('---------------------------------')


for index, item in enumerate(balls):
    print('index :', index, ',item :', item)


print('---------------------------------')


i = 0

while i < len(balls):
    print(balls[i])
    i = i + 1


print('---------------------------------')


print(len(balls)-1)

print(balls.index('탁구공'))

str = 'python'
print(str.index('th'))

balls.append('탁구공')
print(balls)

#12-3 //
hobby = ['독서', '등산', '요리']
hobby.append('배구')
hobby.insert(1, '노래')

print('홍길동 학생의 취미 :', hobby)


print('--------------------------------------------')


numbers = [1, 2, 3, 4, 5, 7, 8, 9]
numbers.append(10)
numbers.insert(5, 6)


print('numbers :', numbers)

#13 rest //

#14-1 //
sports = ['축구', '야구', '배구']

sports.append('농구')
sports.insert(3, '탁구')

print(sports)


list1 = [1, 2, 3]
list2 = [10, 20, 30]
list3 = [100, 200, 300]

print(list1)
print(list2)
print(list3)

list1.extend(list2)

print(list1)


list2 = list2 + list3

print(list2)

print(sports)
print(sports.pop(2))
print(sports)



del sports[2]
print(sports)



sports.remove('농구')
print(sports)

#14-2 //
languages = ['java', 'c/c++', 'c#', 'java', 'c#']
print(languages)

for str in languages:
    if str == 'java':
        languages.remove('java')
print(languages)



while ('c#' in languages):
    languages.remove('c#')
print(languages)



fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
print('fruits : ', fruits)

for item in fruits:
    if item == '당근' or item == '토마토':
        fruits.remove(item)
print('fruits : ', fruits)

#14-3 //
names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
print(names)

names.sort()
print('오름차순 : ', names)

names.sort(reverse = True)
print('내림차순 : ', names)

names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
print(names)

names.reverse()
print('역순 : ', names)



animals = ['호랑이', '사자', '곰', '여우', '늑대']
print(animals)
print(animals[1 : 4])
print(animals[: 3])
print(animals[3 :])
print(animals[len(animals) - 2 :])

#bonus-1 //
def greet():
    print('안녕하세요.')
    print('반갑습니다~.')
    print('저는 박지호입니다.')

print('본문 시작')
greet()
greet()
greet()

#bonus-2 //
def fun1():
    print('fun1 함수를 호출합니다!')

def fun2():
    print('fun2 함수를 호출합니다!')

def fun3():
    fun1()
    fun2()
    print('fun3 함수를 호출합니다!')

fun3()

#bonus-3 //
num = 10

def fun1():
    global num
    num = 20
    print('함수 안 num', num)

print('함수 밖 num', num)
fun1()
print('함수 밖 num', num)

print('----------------------------')

def greet(age, name, pay=200):
    print(age, '세', name, '씨, 안녕하세요.')
    print('월급:', pay)
    print()

greet(20, '홍길동', 400)
greet(pay = 300, age = 22, name = '박찬호')
greet(35, '박지성')

print('--------------------------------------')

def addFunction(n1, n2):
    sum = n1 + n2
    return sum

result = addFunction(10, 20)
print(result)

print('--------------------------------------------')

def add(n1, n2):
    print(n1 + n2)

add(10, 20)

print('---------------------------------------------')

def increaseStar():
    print('*')
    print('**')
    print('***')
    return
    print('****')
    print('*****')
    print('******')
    print('*******')
increaseStar()
    
#The_End //