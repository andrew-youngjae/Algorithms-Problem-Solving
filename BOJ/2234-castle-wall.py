from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(cur_x, cur_y):
    queue = deque()
    queue.append([cur_x, cur_y])
    visited[cur_y][cur_x] = True
    roomSize = 1
    while queue:
        cur_loc = queue.popleft()
        wall = 1
        for i in range(4):
            next_x = cur_loc[0] + dx[i]
            next_y = cur_loc[1] + dy[i]
            if next_x >= 0 and next_x < N and next_y >= 0 and next_y < M:
                if walls[cur_loc[1]][cur_loc[0]] & wall != wall and visited[next_y][next_x] == False:
                    queue.append([next_x, next_y])
                    visited[next_y][next_x] = True
                    roomSize += 1
            wall *= 2
    return roomSize
                
N, M = map(int, input().split())
walls = []
for _ in range(M):
    line = list(map(int, input().split()))
    walls.append(line)

visited = [[False] * N for _ in range(M)]

roomCnt = 0
maxRoomSize = 0
for y in range(M):
    for x in range(N):
        if visited[y][x] == False:
            roomCnt += 1
            maxRoomSize = max(maxRoomSize, bfs(x, y))

maxRoomSizeAfterDel = 0

for y in range(M):
    for x in range(N):
        deletedWall = 1
        while deletedWall < 9:
            if walls[y][x] & deletedWall == deletedWall:
                visited = [[False] * N for _ in range(M)]
                walls[y][x] -= deletedWall
                maxRoomSizeAfterDel = max(maxRoomSizeAfterDel, bfs(x, y))
                walls[y][x] += deletedWall
            deletedWall *= 2

print(roomCnt)
print(maxRoomSize)
print(maxRoomSizeAfterDel)