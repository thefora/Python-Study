from collections import deque
import sys
input = sys.stdin.readline

queue = deque([])

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])

def bfs():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if (0 <= nx < N) and (0 <= ny < M) and (tomato[nx][ny] == 0):
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])

bfs()
max_ = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit()
            
        max_ = max(j, max_)

print(max_ - 1)


