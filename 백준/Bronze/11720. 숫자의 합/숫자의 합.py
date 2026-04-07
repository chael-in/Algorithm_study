import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().strip()))

answer = 0
for i in range(n):
    answer += numbers[i]

print(answer)
