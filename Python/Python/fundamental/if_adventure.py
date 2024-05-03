print('당신은 다음 날, 오전 9시까지 학교에 가야 합니다.')
print('현재 시각은 오후 10시 19분..')
print('당신은 슬슬 잠자리에 들고자 합니다.')
print('')
print('몇 시에 알람을 맞추시겠습니까?')

yourAlarm = int(input('1) 오전 4시 2) 오전 6시 3) 오후 7시 4) 오전 8시  :   '))
if yourAlarm == 1:
    print('당신은 너무 일찍 일어났습니다!')
    print('피로도가 쌓였습니다.')
    print('')
    print('더 주무시겠습니까?')
    moreSleep = int(input('1) YES 2) NO :  '))
    
    if moreSleep == 1:
        print('당신은 다시 잠에 듭니다...')
        print('시간이 흐릅니다...')
        print('시간이 흐릅니다...')
        print('시간이 흐릅니다...')
        print('시간이...?')
        print('저런! 너무 오래 자서 오전 11시가 되었습니다!')
        print('GAME OVER')
    
    elif moreSleep == 2:
        print('일어난 김에 활동하기를 선택하셨습니다.')
        print('')
        print('무엇을 할까요?')
        morning = int(input('1) 씻는다 2) 물을 마신다 3) 휴대폰을 본다 :  '))
