import sys

n = int(sys.stdin.readline())
li = []

for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    li.append((start, end))
    
li.sort(key = lambda x:(x[1], x[0]))

count = 1
end = li[0][1]
for i in range(1, n):
    if li[i][0] >= end:
        end = li[i][1]
        count += 1
        
print(count)