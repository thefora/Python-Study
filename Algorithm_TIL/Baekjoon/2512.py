import sys
input = sys.stdin.readline

N = int(input())
costs = list(map(int, input().split()))
M = int(input())

start = 0
end = max(costs)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    sum = 0
    for cost in costs:
        sum += min(mid, cost)
    
    if sum <= M:
        result = mid
        start = mid + 1
    
    else:
        end = mid -1
        
print(result)
