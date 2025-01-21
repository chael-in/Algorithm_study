n = int(input())

li = []

for i in range(n):
    li.append(list(map(int, input().split())))

d = [[0] * 3 for i in range(n)]

d[0] = li[0]

for i in range(1, n):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + li[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + li[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + li[i][2]

print(min(d[n-1]))
    