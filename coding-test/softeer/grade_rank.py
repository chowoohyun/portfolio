# 인증평가 5차 기출 성적 평가
# 20번까지는 통과 하지만 21번 부터는 시간제한 초과..
# 문제는 3중 for 문 인것 같다.
# idx 를 활용해야 되나...

n = int(input())

score = [list(map(int, input().split())) for _ in range(3)]

total_score = [0] * n

for i in range(len(score)):
    result = []
    for j in range(n):
        rank = 1
        total_score[j] += score[i][j]
        for k in range(n):
            if score[i][j] < score [i][k]:
                rank += 1
        result.append(rank)
    print(*result)

total_rank = []
for a in range(n):
    rank = 1
    for b in range(n):
        if total_score[a] < total_score[b]:
            rank += 1
    total_rank.append(rank)
print(*total_rank)

# 2번째 풀이
# 3개의 대회만 열리기 때문에 min mac 값으로 계산하기
# 동점자 처리에서 에러가 있는듯 하다

for i in score:
    max_score = max(i)
    min_score = min(i)
    for j in range(n):
        total_score[j] += i[j]
        if i[j] == max_score:
            i[j] = 1
        elif i[j] == min_score:
            i[j] = n
        else:
            i[j] = 2
    print(*i)

total_rank = []
for a in range(n):
    rank = 1
    for b in range(n):
        if total_score[a] < total_score[b]:
            rank += 1
    total_rank.append(rank)
print(*total_rank)



# 3번째 풀이
# 3중 for 문을 2중 for 문으로 줄였다.
# 4 ~ 13 번까지가 시간 초과가 뜬다.... 뭐냐

for i in score:
    for j in range(n):
        total_score[j] += i[j]
    sort_score = sorted(i, reverse=True)
    rank = []
    for k in range(n):
        rank.append(sort_score.index(i[k]) + 1)
    print(*rank)

total_rank = []
for a in range(n):
    rank = 1
    for b in range(n):
        if total_score[a] < total_score[b]:
            rank += 1
    total_rank.append(rank)
print(*total_rank)