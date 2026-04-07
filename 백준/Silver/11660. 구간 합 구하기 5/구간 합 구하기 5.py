import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
D = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i-1][j] + D[i][j-1] + graph[i-1][j-1] - D[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    answer = D[x2][y2] - D[x2][y1-1] - D[x1-1][y2] + D[x1-1][y1-1]
    print(answer)
