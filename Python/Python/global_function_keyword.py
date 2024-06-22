total = 0 # 전역 변수 선언

def add_to_total(a, b):
    global total # 전역 변수 total 사용 선언
    total = a + b # 전역 변수 total 수정
    
add_to_total(3, 5)
print('두 수의 합 :', total)