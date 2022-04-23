## codeup 6093
## 이상한 출석 번호 부르기 2
## 거꾸로 출력 하기

# n = int(input())
# m = list(map(int, input().split()))
# for i in range(n-1, -1 , -1):
#     print(m[i],end=' ')


# cnt = int(input())
# num = input().split()

# for i in range(cnt):
#     num[i] = int(num[i])

# for i in range(cnt-1, -1, -1):
#     print(num[i],end=' ')


##codeup6097
##설탕 과자 뽑기
'''
부모님과 함께 놀러간 영일이는
설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
(잉어, 붕어, 용 등 여러 가지가 적혀있다.)

격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

input data : 3(l),1(d),2(x),3(y)

'''
h, w = map(int, input().split())

m=[[0]*w for _ in range(h)]

n = int(input())


for i in range(n):
    l, d, x, y =map(int,input().split())
    if ( d== 0):
        for j in range(l):
            m[x-1][y-1+j] = 1
    else:
        for j in range(l):
            m[x-1+j][y-1] =1
    


for i in range(h):
    for j in range(w):
        print(m[i][j], end=' ')
    print()



###################################################
'''
2차원 배열 만드는 방법에 대해서 다른 방법을 배울수 있어서 좋았다.
하지만 문제에서는 1,1 부터 시작이기 때문에 +- 해줘야 하는것을 까먹어서 오류가 났었지만 하나씩 출력해보면서 작성 해서 결국엔 x-1,y-1로 해결 책을 제시하여 문제를 해결 하였다.

'''