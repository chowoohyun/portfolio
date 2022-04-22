####codeup 6096
##바둑알 십자 뒤집기

'''
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.


'''

#2차원 배열 만들기

d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[j])

#뒤집을 번호 입력 받고, for문을 통해 위아래로 이동하면서 0은 1로 1은 0으로 바꿔주기
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    for j in range(1, 20):
        if d[j][y]== 0:
            d[j][y] = 1
        else:
            d[j][y] =0

        if d[x][j] == 0:
            d[x][j] = 1
        else:
            d[x][j] = 0


#출력하기

for i in range(1,20):
    for j in range(1,20):
        print(d[i][j], end=' ')
    print()






# for i in range(n):
#     x, y = input().split()
#     for j in range(1,20):
#         if 