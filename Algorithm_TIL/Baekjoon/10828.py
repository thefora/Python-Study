import sys

def stack(cmd):
    if "push" in cmd:
        cmd = cmd.split()
        stack_list.append(cmd[1])
        
    elif cmd == "pop":
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list.pop())
        
    elif cmd == "size":
        print(len(stack_list))
        
    elif cmd == "empty":
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)
            
    else:
        if len(stack_list) == 0:
            print(-1)
        else:
            print(stack_list[-1])
            
N = int(input())

stack_list = []
for _ in range(N):
    stack(sys.stdin.readline().rstrip())
