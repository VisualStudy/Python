# [?] n명의 국어 점수 중에서 80점 이상인 점수의 합계

# [1] Input: n명의 국어 점수
scores = [100, 75, 50, 37, 90, 95]
sum = 0

# [2] Process: 합계 알고리즘 영역
for score in scores:
    if score >= 80:
        sum += score

# [3] Output:
print(f"{len(scores)}명의 점수 중 80점 이상의 총점: {sum}")        