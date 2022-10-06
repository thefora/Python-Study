N = int(input())
P = list(map(int, input().split()))
P.sort()

tmp = 0
result = []
for i in P:
    tmp += i
    result.append(tmp)

print(sum(result))
