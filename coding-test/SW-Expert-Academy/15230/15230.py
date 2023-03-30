T = int(input())

al = 'abcdefghijklmnopqrstuvwxyz'

for tc in range(1, T+1):
    str_input = list(map(str, input()))
    cnt = 0
    for i in range(len(str_input)):
        if al[i] == str_input[i]:
            cnt += 1
        else:
            break
    print(f'#{tc} {cnt}')