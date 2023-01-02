# 백준 14725
# 문제: 개미굴


n = int(input())
tree = {}

for _ in range(n):
    k = int(input())
    path = list(input().split())
    current = tree
    for p in path:
        if p not in current:
            current[p] = {}
        current = current[p]

def dfs(tree, depth):
    for key in sorted(tree.keys()):
        print("--"*depth + key)
        dfs(tree[key], depth+1)

dfs(tree, 0)
