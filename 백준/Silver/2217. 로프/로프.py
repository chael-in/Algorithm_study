n = int(input())
li = []

for i in range(n):
    li.append(int(input()))
    
li.sort(reverse=True)

for i in range(n):
    li[i] = li[i] * (i+1)
    
print(max(li))