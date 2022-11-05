import sys
input = sys.stdin.readline

n = int(input())

stack = []
result = []
cnt = 1
flag = True

for _ in range(n):
    num = int(input())
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        flag = False
        break

if flag == True:
    print("\n".join(result))        
