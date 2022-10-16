import sys
input = sys.stdin.readline

N, M = map(int, input().split())
length = list(map(int, input().split()))

start = max(length)
end = 100000*100000*10000
result = 10**9

while start <= end:
    mid = (start + end) // 2

    saved = cnt = 0
    for i in length:
        if saved + i <= mid:
            saved += i 

        else:
            saved = i
            cnt += 1
    
    if saved:
        cnt += 1
    
    if cnt > M:
        start = mid + 1
        
    else:
        result = min(mid, result)
        end = mid - 1

print(result)
