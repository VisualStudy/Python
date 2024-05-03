jump_rope = int(input('당신이 멈추지 않고 할 수 있는 줄넘기 횟수를 입력하세요 :  '))

if jump_rope >= 1000:
    print('와우! 실력자네요!')
    
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