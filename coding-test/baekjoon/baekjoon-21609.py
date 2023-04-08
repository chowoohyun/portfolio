# baekjoon 21609번 상어 중학교

#while 문?
#

# 90도 회전 아이디어가 떠오르지 않아서 블로그 참고
# zip 으로 회전가능 신박하다

from collections import deque
def bfs(x, y, color):
    q = deque()
    q.append([x, y])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    cnt_block, cnt_rain = 1, 0
    blocks, rains = [[x, y]], []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if board[nx][ny] == color:
                        visited[nx][ny] = True
                        q.append([nx, ny])
                        blocks.append([nx, ny])
                        cnt_block += 1
                    elif board[nx][ny] == 0:
                        rains.append([nx, ny])
                        cnt_rain += 1