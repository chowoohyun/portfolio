####codeup 6098
#성실한 개미
#리스트를 이용해서 풀어보는게 좋을거 같다.
#외벽은 1로 해놓고
#2,2에서 출발, 9를 만나면 먹이를 찾는거라 정지
#2차원 배열을 이용해서 풀어야 한다.


# m = []

# for i in range(12):
#     m.append([])
#     for j in range(12):
#         m[i].append(0)

# for i in range(10):
#     a=input().split()
#     for j in range(10):
#         m[i+1][j+1] = int(a[j])
    
# x, y = 2, 2  #시작지점
# while True :
#     if m[x][y] == 0 :
#         m[x][y] = 9
#     elif m[x][y] == 2:
#         m[x][y] = 9
#         break

#     if (m[x][y+1] ==1 and m[x+1][y]==1 or (x==9 and y==9)):
#         break

#     if m[x][y+1] != 1:
#         y +=1
#     elif m[x+1][y] !=1:
#         x +=1


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(m[i][j],end = '')
#     print()



### 직접 짜본 코딩
# m = []

# for i in range(10):
#     m.append(list(map(int, input().split())))

# x, y = 1, 1
# while True:
#     if ( m[x][y]==0):
#         m[x][y] = 9
#     elif ( m[x][y] == 2):
#         m[x][y]=9
#         break

#     if ((m[x][y+1])==1 and m[x+1][y]==1):
#         break

#     if(m[x][y+1] !=1):
#         y += 1
#     elif( m[x+1][y] !=1):
#         x += 1

# for i in range(10):
#     for j in range(10):
#         print(m[i][j], end='')
#     print()