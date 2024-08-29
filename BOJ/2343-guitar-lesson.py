import sys

input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

start = 0
end = 0

for i in lessons:
    if start < i:
        start = i
    end += i

while start <= end:
    mid = int((start + end) / 2)
    size = 0
    numV = 0
    for lesson in lessons:
        if size + lesson > mid:
            numV += 1
            size = 0
        size += lesson
    if size != 0:
        numV += 1
    if numV > M:
        start = mid + 1
    else:
        end = mid - 1

print(start)