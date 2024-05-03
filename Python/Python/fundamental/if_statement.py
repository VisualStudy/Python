jump_rope = int(input('당신이 멈추지 않고 할 수 있는 줄넘기 횟수를 입력하세요 :  '))

if jump_rope >= 1000:
    print('와우! 실력자네요!')
    areYou = int(input('혹시 운동선수인가요? 1) YES 2) NO :  '))
    if areYou == 1:
        print('멋저요! 운동선수였군요!')
        youAre = input('혹시 어떤 종목인가요? 입력해주세요 :  ')
        print(youAre,', 멋진 종목이네요!') 
    else:
        print('운동선수가 아닌데 이 정도의 실력? 당신은 이미 일반인이 아니군요..')

elif jump_rope >=500:
    print('오호라~ 평소 운동을 하시나 보군요!')
    
elif jump_rope >=100:
    print('제법인걸요?')
    
elif jump_rope >=50:
    print('나쁘진 않지만 분발합시다!')
    
elif jump_rope > 0:
    print('저런! 건강을 지킵시다!')
    
elif jump_rope == 0:
    print('정말로 한 개도 못하시나요? 이번 기회에 배워봅시다!')
    
else:
    print('.....음수라도 입력하신 건가요?')