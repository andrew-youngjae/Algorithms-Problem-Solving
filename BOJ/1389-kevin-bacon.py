import sys
from collections import deque

input = sys.stdin.readline

def bfs(cur_p):
    queue = deque()
    queue.append(cur_p)
    friend_dist = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    friend_dist[cur_p] = 0
    visited[cur_p] = True
    while queue:
        cur_f = queue.popleft()
        for friend in network[cur_f]:
            if visited[friend] == False:
                queue.append(friend)
                friend_dist[friend] = friend_dist[cur_f] + 1
                visited[friend] = True

    return friend_dist


N, M = map(int, input().split())
network = [[] for _ in range(N+1)]

for _ in range(M):
    person, friend = map(int, input().split())
    network[person].append(friend)
    network[friend].append(person)

kevin_bacon = [0 for _ in range(N+1)]

for i in range(1, N+1):
    friend_dist = bfs(i)
    kevin_bacon[i] = sum(friend_dist)

min = 5001
min_idx = 0
for j in range(1, N+1):
    if kevin_bacon[j] < min:
        min = kevin_bacon[j]
        min_idx = j

print(min_idx)