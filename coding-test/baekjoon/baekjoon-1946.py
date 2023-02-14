#https://www.acmicpc.net/problem/1946
#백준 신입사원
# 실버1
# 입력값 잘 확인하기
# 점수가 아니라 등수다.

n = int(input())

for _ in range(n):
    cnt = 1
    arr = []
    m = int(input())
    for _ in range(m):
        arr.append(list(map(int, input().split())))
    
    arr.sort(key= lambda x:x[0])
    # 1등은 무조건 뽑히니 ant = 1
    # 그뒤 1등보다 다른 등수가 높은 사람을 뽑아야 하니 for문으로 비교 해서 cnt 업데이트
    min = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][1] < min:
            min = arr[i][1]
            cnt += 1
    print(cnt)


'''
N = int(input())
for _ in range(N):
    cnt = 1
    arr = []
    M = int(input())
    for _ in range(M):
        arr.append(list(map(int, input().split())))
    arr.sort(key= lambda x:x[0])
    min = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][1] < min:
            min = arr[i][1]
            cnt += 1
    print(cnt)
'''