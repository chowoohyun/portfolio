main_str = input()
answer = []

for i in range(1, len(main_str)+1):
    for j in range(len(main_str)-i+1):
        answer.append(main_str[j:j+i])

print(len(set(answer)))
