# https://www.acmicpc.net/problem/1260
# DFS BFS

# DFS = 깊이 우선 탐색 - 아래로
# BFS = 넓이 우선 탐색 - 옆으로

n, m, v = map(int, input().split())
matrix = [[0]*(n-1) for _ in range(n+1)]
visit = [False] * ( n-1)

for _ in range(m):
    f, t = map(int, input().split())
    matrix[f][t] = matrix[t][f] = 1


def dfs(matrix, i, visit):
    visit[i] = True
    print(i, end=' ')
    for c in range(len(matrix[i])):
        if matrix[i][c] == 1 and not visit[c]:
            dfs(matrix, c, visit)

from collections import deque

def bfs(matrix, i, visit):
    return 0
