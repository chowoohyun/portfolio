T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print(N)
    i , j = 1, 1
    
    while i * j < N:
        print(f'#{tc} {i} {j}')
        