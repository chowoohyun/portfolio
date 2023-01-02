# 스택 수열
# https://www.acmicpc.net/problem/1847
# 이해가 어렵다

n = int(input())
stack = []
result = []
cnt = 1
tmp = True

for i in range(n):
    num = int(input())

    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')

    else:
        tmp = False
        break

if tmp == False:
    print('NO')
else:
    for i in result:
        print(i)
