import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())

def dfs(node, group):
    global flag
    visit[node] = group
    for neighbor in arr[node]:
        if visit[neighbor] == 0:
            dfs(neighbor, 3 - group)
        elif visit[node] == visit[neighbor]:
            flag = 0
            return

for _ in range(T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V + 1)]
    visit = [0] * (V + 1)
    flag = 1

    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, V + 1):
        if visit[i] == 0 and flag:
            dfs(i, 1)

    if flag:
        print('YES')
    else:
        print('NO')