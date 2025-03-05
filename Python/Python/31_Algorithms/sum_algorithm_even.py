# [?] n명의 국어 점수 중에서 80점 이상인 점수의 합계

# [1] Input: n명의 국어 점수
scores = [100, 75, 50, 37, 90, 95]
sum = 0

# [2] Process: 합계 알고리즘 영역
for score in scores:
    if score % 3 == 0 or score % 4 == 0:
        sum += score

# [3] Output:
print(f"{len(scores)}명의 점수 중 3의 배수 또는 4의 배수의 총점: {sum}")        