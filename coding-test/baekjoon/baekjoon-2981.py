N = int(input())

num_list = []
answer = []
for _ in range(N):
    num_list.append(int(input()))


for i in range(2, num_list[-1]):
    num_list = [num % i for num in num_list]
    if len(set(num_list)) == 1:
        answer.append(i)
        print(i, answer)
    else:
        continue

for i in answer:
    print(i, end=' ')

