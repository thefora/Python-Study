import sys
input = sys.stdin.readline

n = int(input())
h_i = list(map(int, input().split()))
a_i = list(map(int, input().split()))

idx = [i for i in range(n)]

sorted_idx = sorted(idx, key = lambda x : a_i[x])

result = 0
for idx_num, idx in enumerate(sorted_idx):
    result += h_i[idx] + a_i[idx] * idx_num

print(result)
