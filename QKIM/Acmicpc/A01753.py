import sys, heapq
input = sys.stdin.readline
# constant
INF = 12345678
# input
v, e = map(int, input().split())
k = int(input())
V = [[] for _ in range(v + 1)]
for _ in range(e):
	v1, v2, w = map(int, input().split())
	V[v1].append((v2, w))

# process
'''
다익스트라 알고리즘 사용
'''
visited = set()
h = [(INF, i) for i in range(v + 1)]
h[k] = (0, k)
heapq.heapify(h)
dist = [INF for _ in range(v + 1)]
dist[k] = 0

while h:
	_, cur = heapq.heappop(h)
	if cur in visited: continue
	visited.add(cur)
	for adj, w in V[cur]:
		if adj in visited: continue
		if dist[cur] + w < dist[adj]:
			dist[adj] = dist[cur] + w
			heapq.heappush(h, (dist[adj], adj))

# output
for i in range(1, v + 1):
	print(dist[i] if dist[i] != INF else "INF")