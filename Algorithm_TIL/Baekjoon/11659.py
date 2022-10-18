import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num = list(map(int, input().split()))
section = [list(map(int, input().split())) for _ in range(M)]

pnum = [num[0]]
for i in range(1, N):
    pnum.append(pnum[i-1] + num[i])

result = []
for i in section:
    if i[0] != 1:
        result.append(pnum[i[1] - 1] - pnum[i[0] - 2])

    else:
        result.append(pnum[i[1] - 1])

print(" ".join(map(str, result)))
