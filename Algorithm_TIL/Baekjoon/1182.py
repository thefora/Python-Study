from itertools import combinations
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
num = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    for j in list(combinations(num, i)):
        if sum(j) == S:
            cnt += 1

print(cnt)
