import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
heights = list(map(int, sys.stdin.readline().rstrip().split()))

low = 0
high = max(heights)

result = 0
while low <= high:
    total = 0
    cut = (low + high) // 2
    total = sum([i-cut if i-cut > 0 else 0 for i in heights])
    
    if total < M:
        high = cut - 1
    
    else:
        result = cut
        low = cut + 1
    
print(result)
