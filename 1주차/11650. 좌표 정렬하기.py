n = int(input())

li = []

# 이중 리스트로 저장
for i in range(n):
    [a, b] = map(int, input().split())
    li.append([a, b])


# sort 정렬
li.sort()
for i in li:
    print(i[0], i[1])