import sys
input = sys.stdin.readline

def sum_of_sector(arr, sector):
    for i in sector:
        if i[0] != 1:
            print(arr[i[1] - 1] - arr[i[0] - 2])
        else:
            print(arr[i[1] - 1])

N = int(input())
A = list(map(int, input().split()))
M = int(input())
sector = [list(map(int, input().split())) for _ in range(M)]

for i in range(1, len(A)):
    A[i] += A[i-1]

sum_of_sector(A, sector)
