# 현재 회의실에서 회의가 끝나는 시간보다 다음 회의의 시작 시간이 빠르면 회의실 하나를 추가로 개설
# 회의가 끝나는 시간보다 다음 회의의 시작 시간이 느리면 현재 회의실에서 이어서 회의

# 우선순위 큐 활용
import heapq
import sys

# 입력받은 문자열을 정수로 변환하여 n에 저장
n = int(input())

# 시간초과
# # 빈 리스트 q 생성, 회의의 시작시간과 종료시간 저장
# q = []

# # 입력받은 정수 a, b를 리스트로 묶어 q에 추가, n번 반복
# for i in range(n):
#     [a, b] = map(int, input().split())
#     q.append([a, b])

n = int(input())
q = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# q 리스트 정렬, 시작 시간을 기준으로 오름차순 정렬
q.sort()

# 빈 리스트 room 생성
room = []
# 첫 번째 회의의 종료시간을 최소 힙 room에 추가
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]: # 다음 회의의 시작시간이 현재 회의실의 끝나는 시간보다 빠르면
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설, 다음 회의의 종료 시간을 room 힙에 추가
    else: # 현재 회의실에서 이어서 회의한다면
        heapq.heappop(room) # 빨리 끝나는 회의실의 종료 시간 pop (제거)
        heapq.heappush(room, q[i][1]) # 다음 회의의 종료시간을 room 힙에 추가

# 회의실의 개수 출력
print(len(room))