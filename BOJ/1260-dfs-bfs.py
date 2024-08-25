N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

vdfs = [0]*(N+1)
vbfs = [0]*(N+1)

def dfs(curV):
    vdfs[curV] = 1
    print(curV, end=' ')
    for i in range(1, N+1):
        if (graph[curV][i] == 1 and vdfs[i] == 0):
            dfs(i)

def bfs(curV):
    queue = [curV]
    vbfs[curV] = 1   
    while queue:
        curV = queue.pop(0)
        print(curV, end=' ')
        for i in range(1, N+1):
            if(graph[curV][i] == 1 and vbfs[i] == 0):
                queue.append(i)
                vbfs[i] = 1

dfs(V)
print()
bfs(V)