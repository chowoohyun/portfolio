#https://www.acmicpc.net/problem/1966

from collections import deque

t_c = int(input())

for _ in range(t_c):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    idx = list(range(len(p)))
    idx[m] = 'end'

    answer = 0

    while True:

        if p[0] == max(p):
            answer += 1

            if idx[0] == 'end':
                print(answer)
                break
            else:
                p.pop(0)
                idx.pop(0)
        else:
            p.append(p.pop(0))
            idx.append(idx.pop(0))
    
