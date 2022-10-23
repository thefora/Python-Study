import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))


for i in range(1, N):
    A[i] += A[i-1]

cnt = {}
result = 0
for i in range(N):
    target = A[i] - M

    if target in cnt:
        result += cnt[target]
    
    if target == 0:
        result += 1
    
    if A[i] not in cnt:
        cnt[A[i]] = 0
    cnt[A[i]] += 1
    
print(result)
