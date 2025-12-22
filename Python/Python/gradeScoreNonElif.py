score = int(input('성적을 입력하시오: '))

if score >= 0 and score <= 100:
    if score >= 90:
        print('A')
    else:
        if score >= 80:
            print('B')
        else:
            if score >= 70:
                print('C')
            else:
                if score >= 60:
                    print('D')
                else:
                    print('F')
else:
    print('잘못된 입력입니다. 성적은 0점~100점까지입니다.')