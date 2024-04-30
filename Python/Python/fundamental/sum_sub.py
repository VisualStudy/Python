10 + 10     # output : 20 // 정수(int) + 정수(int) = 정수(int)

3.2 + 3.2   # output : 6.4 // 실수(float) + 실수(float) = 실수(float)

10 + 9.9    # output : 19.9 // 정수(int) + 실수(float) = 실수(float)

10 + 9.0    # output : 19.0 // 정수(int) + 실수(float) + 실수(float) 
            # /* 소수점 자리가 의미 없는 실수여도 정수 + 실수 = 실수이다. */

'a' + 'b'   # output : ab

'nice' + ' ' + 'to' + ' ' + 'meet' + ' ' + 'you' 
            # output : nice to meet you

'nice' + 1  # ERROR!

10 - 5      # output : 5

3.14 - 0.1  # output : 3.04

3.14 - 0.14 # output : 3.0

'hhi' - 'h' # ERROR!