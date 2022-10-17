import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]

num.sort()

dif = 0
for i in range(1, n-1):
    left = num[0] + num[i] + num[i+1]
    right = num[i-1] + num[i] + num[n-1]
    if dif < max(abs(left - 3 * num[i]), abs(right - 3 * num[i])):
        dif = max(abs(left - 3 * num[i]), abs(right - 3 * num[i]))

print(dif)
