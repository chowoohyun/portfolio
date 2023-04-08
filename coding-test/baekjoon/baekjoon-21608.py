N = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

jari = [[0] * (N+1) for _ in range(N+1)]
input_jari = []


for _ in range(N**2):

    list_input = list(map(int, input().split()))
    student = list_input[0]
    like = list_input[1:]
    input_jari.append(list_input)
    result = []

    for i in range(1, N+1):
        for j in range(1, N+1):

            if jari[i][j] == 0:
                cnt = 0
                cnt_like = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 1<=nx < N+1 and 1<=ny < N+1:
                        if jari[nx][ny] in like:
                            cnt_like += 1
                        if jari[nx][ny] == 0:
                            cnt += 1

                #참고 - 블로그
                result.append([cnt_like, cnt, i, j])

    #참고 - 블로그
    result = sorted(result, key=lambda x: (-x[0], -x[1], x[2], x[3]))
    jari[result[0][2]][result[0][3]] = student

# 이때 이미 1시간
# 뽑아내는 방법 생각 부족
input_jari.sort()

sum = 0
for i in range(1, N+1):
    for j in range(1, N+1):

        count = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if (1 <= nx < N+1 and 1 <= ny < N+1):
                if (jari[nx][ny] in input_jari[jari[i][j]-1]):
                    count += 1

        #참고 - 블로그
        if (count != 0):
            sum += 10**(count-1)

print(sum)