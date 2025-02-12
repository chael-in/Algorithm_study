n = int(input())
m = int(input())

graph = [[]*n for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


count = 0
# 해당 노드에 방문했는지 안했는지 저장하기 위한 visited 배열
visited = [0] * (n+1)

def dfs(start):
    global count
    # start 노드 방문
    visited[start] = 1
    # start와 인접한 노드 탐색
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)
            count += 1

dfs(1)
print(count)