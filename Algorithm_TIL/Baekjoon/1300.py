#### 핵심 ####
# 어떤 수(x)가 k번째 수 라는것은
# x보다 작은 수가 k-1개 이하
# x보다 큰 수가 N(전체 수)-k개 이하 를 만족하는 것이다.

N = int(input())
k = int(input())

low = 1
high = N * N

result = 0
while low <= high:
    mid = (low + high) // 2
    
    below = 0
    above = 0
    
    for i in range(1, N+1):
        below += min(N, ((mid - 1) // i))
    
    for i in range(1, N+1):
        above += N - min(N, (mid // i))
    
    if below > k-1:
        high = mid - 1
    
    elif above > N * N - k:
        low = mid + 1
        
    else:
        result = mid
        break
        
print(result)
