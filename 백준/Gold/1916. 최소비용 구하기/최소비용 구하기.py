import sys
import heapq

# 무한을 의미하는 값
INF = int(1e9)

# 도시 개수, 버스 개수 입력
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 버스 정보를 저장할 그래프 정의
graph = [[] for _ in range(n+1)]

# 최단 거리를 저장할 리스트 정의
distances = [INF] * (n+1)

# 버스 정보 입력
for _ in range(m):
    start, end, weight = map(int, sys.stdin.readline().split())
    # 단방향 그래프
    graph[start].append((end, weight))

# 다익스트라 알고리즘 구현
def dijkstra(start):
    q =[]
    # 시작 도시의 최단 거리는 0
    heapq.heappush(q, (0, start))
    distances[start] = 0

    # 큐가 빌 때까지 반복
    while q:
        # 값이 가장 작은 도시 선택
        distance, city = heapq.heappop(q)
        # 방문한 적 있는 도시라면 무시 (이미 처리된 노드라면 무시)
        if distances[city] < distance:
            continue

        # 연결된 도시 확인
        for next_city, weight in graph[city]:
            new_distance = distance + weight
            
            # 더 짧은 거리라면 갱신
            if new_distance < distances[next_city]:
                distances[next_city] = new_distance
                heapq.heappush(q, (new_distance, next_city))

# 출발지 a, 도착지 b 입력
a, b = map(int, sys.stdin.readline().split())

# 다익스트라 수행
dijkstra(a)

# 도착지 b까지의 최단 거리 출력
print(distances[b])