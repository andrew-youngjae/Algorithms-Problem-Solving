import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))

sum = numList[0]
start = 0
end = 1
count = 0

while True:
    if sum < M:
        if end < N:
            sum += numList[end]
            end += 1
        else:
            break
    elif sum == M:
        count += 1
        sum -= numList[start]
        start += 1
    else:
        sum -= numList[start]
        start += 1

print(count)