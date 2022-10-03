N = int(input())

time = []
for _ in range(N):
    start, end = map(int, input().split(' '))
    time.append([start, end])

time.sort(key= lambda x : (x[1], x[0]))

cnt, target_end = 0, 0
for start, end in time:
    if start >= target_end:
        cnt += 1
        target_end = end

print(cnt)
