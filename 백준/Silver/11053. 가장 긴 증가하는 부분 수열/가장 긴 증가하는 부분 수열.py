n = int(input())

li = list(map(int, input().split()))

# i가 0일 때 증가하는 최대 부분 수열의 길이는 1이기 때문에, 테이블을 우선 전부 1로 초기화
d = [1] * n

for i in range(1, n):
    for j in range(i): # i보다 작은 j 각각에 대해
        if li[i] > li[j]: # j의 원소가 i의 원소보다 작으면, 즉 부분적으로 증가한다면
            d[i] = max(d[i], d[j]+1) # i에서의 최적의 해를 갱신

# 가장 긴 증가하는 부분 수열의 길이 출력
print(max(d)) 