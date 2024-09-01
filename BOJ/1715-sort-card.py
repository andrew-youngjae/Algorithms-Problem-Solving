import sys
from queue import PriorityQueue

input = sys.stdin.readline

N = int(input())
pqueue = PriorityQueue()

for _ in range(N):
    pqueue.put(int(input()))

minsum = 0

while pqueue.qsize() > 1:
    r1 = pqueue.get()
    r2 = pqueue.get()
    temp = r1 + r2
    minsum += temp
    pqueue.put(temp)

print(minsum)