# baekjoon 21609번 상어 중학교

#while 문?
#

# 90도 회전 아이디어가 떠오르지 않아서 블로그 참고
# zip 으로 회전가능 신박하다

from collections import deque
N, M = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for i in range(N):
    li = list(map(int, input().split()))
    for j in range(N):
        arr[i][j] = li[j]
def find_Max():
    global arr, N, M
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visit = [[False]*N for _ in range(N)]
    maxVal = 0
    maxStart = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] is False and arr[i][j] > 0:
                visit[i][j] = True
                now = arr[i][j]
                zeros = []
                q = deque()
                cnt = 1
                q.append((i,j))
                rainbow = 0
                while q:
                    x, y = q.popleft()
                    for l in range(4):
                        xx = dx[l] + x
                        yy = dy[l] + y
                        if 0<=xx<N and 0<=yy<N and (arr[xx][yy] == now or arr[xx][yy] == 0) and visit[xx][yy] is False:
                            visit[xx][yy] = True
                            if arr[xx][yy] == 0:
                                zeros.append((xx,yy))
                                rainbow += 1
                            q.append((xx,yy))
                            cnt += 1
                if cnt >= maxVal:
                    if cnt > maxVal:
                        maxStart = []
                    maxVal = cnt
                    maxStart.append((-rainbow, -i,-j))
                for zero in zeros:
                    visit[zero[0]][zero[1]] = False
    if not maxStart:
        return 0
    if maxVal <= 1:
        return 0
    maxStart.sort()
    maxStart = (-maxStart[0][1], -maxStart[0][2])
    now = arr[maxStart[0]][maxStart[1]]
    q = deque()
    q.append(maxStart)
    visit = [[False] * N for _ in range(N)]
    visit[maxStart[0]][maxStart[1]] = True
    while q:
        x, y = q.popleft()
        arr[x][y] = -2
        for l in range(4):
            xx = dx[l] + x
            yy = dy[l] + y
            if 0 <= xx < N and 0 <= yy < N and (arr[xx][yy] == now or arr[xx][yy] == 0) and visit[xx][yy] is False:
                visit[xx][yy] = True
                q.append((xx, yy))
    return maxVal*maxVal

def grarvity():
    global arr
    # 열별로
    for j in range(N):
        ind = N-1
        for i in range(N-1, -1, -1):
            if arr[i][j] == -2:
                continue
            if arr[i][j] == -1:
                ind = i-1
                continue
            if ind == i:
                ind -=1
                continue
            arr[ind][j] = arr[i][j]
            arr[i][j] = -2
            ind -= 1
def rotate():
    global arr
    res = []
    for j in range(N-1, -1, -1):
        temp = []
        for i in range(N):
            temp.append(arr[i][j])
        res.append(temp)
    arr= res

result = 0
while True:
    score = find_Max()
    result += score
    if score == 0:
        break
    grarvity()
    rotate()
    grarvity()
print(result)