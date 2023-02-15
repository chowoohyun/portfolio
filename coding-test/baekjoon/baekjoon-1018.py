# 백준 1018번 체스판 다시 칠하기
# 브루트포스 알고리즘

N, M = map(int, input.split())

map = []
result = []

for _ in range(N):
    map.append(input())

# 이중 for 문을 통해 체스판 체크
for a in range(N-7):
    for b in range(M-7):
        idx1 = 0
        idx2 = 0
        # 이중 for 문을 통해 w,b 체크 후 idx 에 저장,
        # idx의 가장 작은 값만 가져온다.
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if map[i][j] != 'W':
                        idx1 += 1
                    if map[i][j] != 'B':
                        idx2 += 1
                else:
                    if map[i][j] != 'B':
                        idx1 += 1
                    if map[i][j] != 'W':
                        idx2 += 1
        result.qppend(min(idx1, idx2))

print(min(result))


'''
N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N-7):
    for b in range(M-7):
        index1 = 0
        index2 = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j) % 2 == 0:
                    if original[i][j] != 'W':
                        index1 += 1
                    if original[i][j] != 'B':
                        index2 += 1
                else:
                    if original[i][j] != 'B':
                        index1 += 1
                    if original[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))
'''