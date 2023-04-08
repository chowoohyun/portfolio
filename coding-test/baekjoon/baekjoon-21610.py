N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]
 
dy_8 = ("empty", 0, -1, -1, -1, 0, 1, 1, 1)
dx_8 = ("empty", -1, -1, 0, 1, 1, 1, 0, -1)
 
dy_4 = (-1, -1,  1, 1)
dx_4 = (-1,  1, -1, 1)
 
# 구름 좌표
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in moves:
    
    moving_cloud = []
    for y, x in clouds:
        
        # 아이디어 참고함 행 열 이어지게 하는방법
        ny = (y + dy_8[d] * s) % N 
        nx = (x + dx_8[d] * s) % N
        map[ny][nx] += 1 
        moving_cloud.append((ny, nx)) 
 
    for y, x in moving_cloud:
           
        cnt = 0
        for d in range(4):
            ny = y + dy_4[d]
            nx = x + dx_4[d]
            
            if ny < 0 or nx < 0 or ny >= N or nx >= N: continue
            elif map[ny][nx] > 0: cnt += 1
        map[y][x] += cnt
 
    new_clouds = []
    for y in range(N):
        for x in range(N):
            
            if (y, x) in moving_cloud or map[y][x] < 2:
                continue
            map[y][x] -= 2
            new_clouds.append((y, x))
    clouds = new_clouds 
 
result = 0
for y in range(N):
    for x in range(N):
        result += map[y][x]
print(result)