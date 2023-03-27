T = int(input())

for tc in range(1, T+1):
    n = int(input())
    heights = list(map(int, input().split()))
    cnt = 0
    check = [-1,-2,1,2]
    for i in range(2, n-2):
        check_list = []
        for j in check:
            check_list.append(heights[i+j])

        if heights[i] < max(check_list):
            continue
        cnt += heights[i] - max(check_list)
    print(f'#{tc} {cnt}')

'''
21:34:25 컴파일 오류 :
오류 메세지 :
solution.py, line 46)
21:34:25 Input data가 없으므로 Sample input으로 테스트됩니다.
'''