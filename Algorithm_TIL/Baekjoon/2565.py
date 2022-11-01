import sys
input = sys.stdin.readline

n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]

line = sorted(line, key=lambda x : x[0])

d = [1] * n

for i in range(1, n):
    for j in range(i):
        if line[i][1] > line[j][1]:
            d[i] = max(d[i], d[j] + 1)

print(n-max(d))
