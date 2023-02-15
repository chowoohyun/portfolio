# 인증평가 5차 기출 성적 평가



n = int(input())

arr = [list(map(int, input().split())) for _ in range(3)]

total_score = [0] * n

for i in range(len(arr)):
    result = []
    for j in range(n):
        rank = 1
        total_score[j] += arr[i][j]
        for k in range(n):
            if arr[i][j] < arr [i][k]:
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
