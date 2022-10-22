import sys
input = sys.stdin.readline

N = int(input())
liq = list(map(int, input().split()))

start = 0 
end = len(liq) - 1
min = 2e9 

while start < end:
    x1 = liq[start]
    x2 = liq[end]

    if abs(x1 + x2) < min:
        r1, r2 = x1, x2
        min = abs(x1 + x2)
    
    if abs(x1) > abs(x2):
        start += 1
    
    else:
        end -= 1

print(r1, r2)
