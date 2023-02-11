# baekjoon 1339
# 그리디 알고리즘

N = int(input())

words = [input() for _ in range(N)]

dict = {}
for word in words:
    root = len(word)-1
    for i in word:
        if i in dict:
            dict[i] += 10**root
        else:
            dict[i] = 10**root
        root -= 1
dict = sorted(dict.values(), reverse=True)

result = 0
m = 9

for value in dict:
    result += value*m
    m -= 1

print(result)