N = int(input())

num_list = []
for _ in range(N):
    num_list.append(int(input()))



for j in num_list[-1]:
    for i in range(N-1):
        if num_list[i] % j != num_list[i+1] % j:
            break

        if i == N-2:
            print(j, end=' ')

