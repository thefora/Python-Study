import sys
input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            tri[i][j] = tri[i-1][j] + tri[i][j]
        
        elif j == i:
            tri[i][j] = tri[i-1][j-1] + tri[i][j]
        
        else:
            tri[i][j] = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
        
print(max(tri[n-1]))
