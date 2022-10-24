from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_ = 0
for a in list(permutations(arr)):
    
    total = 0
    for j in range(N-1):
        total += abs(a[j] - a[j+1])
    
    max_ = max(total, max_)

print(max_)
