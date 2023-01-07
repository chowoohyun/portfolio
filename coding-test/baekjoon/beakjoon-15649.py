# N과 M (1)
# https://www.acmicpc.net/problem/15649

n, m = map(int, input().split())

answer = []


def dfs():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()


dfs()
