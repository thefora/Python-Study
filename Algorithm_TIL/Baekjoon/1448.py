import sys
input = sys.stdin.readline

N = int(input())

straws = [int(input()) for _ in range(N)]
straws.sort()

result = -1
for i in range(N-1, 1, -1):
    if straws[i] < straws[i-1] + straws[i-2]:
        result = straws[i] + straws[i-1] + straws[i-2]
        break

print(result)
