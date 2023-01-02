N = int(input())

hansu = 0

for n in range(1, N+1):
    if n <100:
        hansu += 1
    else:
        N = list(map(int, str(n)))
        if N[0] - N[1] == N[1] - N[2]:
            hansu += 1
print(hansu)
