import sys

# 입력값 앞에 공백을 추가해서 저장
str_a = ' ' + sys.stdin.readline().rstrip()
str_b = ' ' + sys.stdin.readline().rstrip()

# dp 사용, dp 테이블 초기화
dp = [[0]*len(str_b) for _ in range(len(str_a))]

for i in range(1, len(str_a)):
    for j in range(1, len(str_b)):
        if str_a[i] == str_b[j]:
            dp[i][j] = dp[i-1][j-1] + 1 # 이전까지의 LCS에 +1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 이전 행 또는 열의 최댓값 가져옴
    
# 최장 공통 부분 수열(LCS)의 길이 출력
print(dp[-1][-1])