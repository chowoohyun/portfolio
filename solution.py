# 백준 그리디 알고리즘 11399번 문제 ATM

N = int(input())
min_list = list(map(int, input().split()))

min_list = sorted(min_list)
answer = 0

for i in range(N):
    answer += sum(min_list[:i+1])

print(answer)
