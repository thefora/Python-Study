import sys
input = sys.stdin.readline

K = int(input())

num = [int(input()) for _ in range(K)]

stack = []

for i in num:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))
    
