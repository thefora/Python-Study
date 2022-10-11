import sys
input = sys.stdin.readline

N, C = map(int, input().split())
x = [int(input()) for i in range(N)]

x.sort()
    
low = 1
high = x[-1] - x[0]
result = 0
while low <= high:
    mid = (low + high) // 2
    
    cnt = 1
    dis = x[0]
    for i in range(1, N):
        if x[i] - dis >= mid:
            cnt += 1
            dis = x[i]
    
    if cnt >= C:
        result = mid
        low = mid + 1
    
    else:
        high = mid - 1

print(result)
