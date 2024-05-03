print('1. 1반 2. 2반 (단, 나머지는 자율전공반이다.)')
yourClass = int(input('귀하의 반을 입력하세요 :  '))


if yourClass == 1:
    print('귀하의 반은 1반입니다.')
    print('성별을 입력해주세요.')
    yourGender = int(input('1. 남자 2. 여자 :  '))
    if yourGender == 1:
        print('귀하의 성별은 남자입니다.')
    elif yourGender == 2:
        print('귀하의 성별은 여자입니다.')
    else:
        print('1 또는 2 중에 해당하는 사항을 입력하세요.')

elif yourClass == 2:
    print('귀하의 반은 2반입니다.')
    print('성별을 입력해주세요.')
    yourGender = int(input('1. 남자 2. 여자 :  '))
    if yourGender == 1:
        print('귀하의 성별은 남자입니다.')
    elif yourGender == 2:
        print('귀하의 성별은 여자입니다.')
    else:
        print('1 또는 2 중에 해당하는 사항을 입력하세요.')
        
else:
    print('귀하의 반은 1반도 2반도 아닌 자율전공반입니다.')
    print('성별을 입력해주세요.')
    yourGender = int(input('1. 남자 2. 여자 :  '))
    if yourGender == 1:
        print('귀하의 성별은 남자입니다.')
    elif yourGender == 2:
        print('귀하의 성별은 여자입니다.')
    else:
        print('1 또는 2 중에 해당하는 사항을 입력하세요.')