## codeup 기초 50제

##6095번
''' 기숙사 생활을 하는 학교에서 어떤 금요일(전원 귀가일)에는 
모두 집으로 귀가를 한다.

오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 
생각해 보다가
"바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.''' 
# arr = []

# for i in range(20):
#     arr.append([])

#     for j in range(20):
#         arr[i].append(0)


# n = int(input())  # 뒤집을 갯수

# for i in range(n):
#     x, y = map(int, input().split())
#     arr[x][y] =1


# for i in range(1,20):
#     for j in range(1,20):
#         print(arr[i][j], end=' ')

#     print()
# n = int(input())


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

# d = []

# for i in range(20):
#     d.append([])

#     for j in range(20):
#         d[i].append(0)

# for i in range(19):
#     a = input().split()
#     for j in range(19):
#         d[i+1][j+1] = int(a[j])

# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())

#     for j in range(1,20):
#         if d[j][y] == 0:
#             d[j][y]== 1
#         else:
#             d[j][y]=0
        
#         if d[x][j] == 0:
#             d[x][j] =1
#         else:
#             d[x][j] = 0
# for i in range(1, 20):
#     for j in range(1, 20):
#         print(d[i][j], end = ' ')
#     print()

        

#######프로그래머스 level 1 모의고사

# def solution(answers):
    
#     cnt1 ,cnt2, cnt3 = 0, 0, 0
#     score = [0, 0, 0]
#     stu1 = [1,2,3,4,5]
#     stu2 = [2,1,2,3,2,4,2,5]
#     stu3 = [3,3,1,1,2,2,4,4,5,5]
    
    
    
#     for i in range(len(answers)):
#         if answers[i] == stu1[i%len(stu1)]:
#             cnt1 += 1
#         if answers[i] == stu2[i%len(stu2)]:
#             cnt2 += 1
#         if answers[i] == stu3[i%len(stu3)]:
#             cnt3 += 1
            
            
#     result= max(cnt1, cnt2, cnt3)
#     answer=[]
    
#     if result == cnt1:
#         answer.append(1)
#     if result == cnt2:
#         answer.append(2)
#     if result == cnt3:
#         answer.append(3)
        
#     return answer