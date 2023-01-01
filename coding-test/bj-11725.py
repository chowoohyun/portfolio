# 백준 11725
# 트리
# deque 사용하는 방법으로 풀었음 ~

from collections import deque
N = int(input())
visited = [0] * (N + 1)
ans = [0] * (N + 1)
a = dict()
for i in range(1, N + 1):
    a[i] = set()

for i in range(N-1):
    x, y = map(int, input().split())
    a[x].add(y)
    a[y].add(x)

q = deque()
q.append((1))
while q:
    x = q.popleft()
    for i in a[x]:
        if visited[i] != 1:
            ans[i] = x
            q.append(i)
            visited[i] = 1
for i in range(2, N+1):
    print(ans[i])
