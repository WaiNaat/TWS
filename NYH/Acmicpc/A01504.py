import sys
import heapq

INF = 1e9
class Node:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight
    
    def __lt__(self, other):
        if self.weight < other.weight:
            return True
        else:
            False

def input():
    return sys.stdin.readline().rstrip()
    

def dijkstra(start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    heapq.heappush(heap, Node(start, 0))

    while heap:
        cur_node = heapq.heappop(heap)

        if dist[cur_node.to] < cur_node.weight:
            continue

        for i in range(1, len(graph[cur_node.to])):
            adj_node = graph[cur_node.to][i]
            if dist[adj_node.to] > cur_node.weight + adj_node.weight:
                dist[adj_node.to] = cur_node.weight + adj_node.weight
                heapq.heappush(heap, Node(adj_node.to, dist[adj_node.to]))

    return dist[end]

if __name__ == "__main__":
    # 끝 정점, 간선 개수
    N, E = map(int,input().split())
    # 간선
    data = [list(map(int, input().split())) for _ in range(E)]
    # 무조건 지나야 하는 두개의 정점
    V1, V2 = map(int,input().split())
    
    graph = [[0] for _ in range(N + 1)]
    for i in range(len(data)):
        graph[data[i][0]].append(Node(data[i][1], data[i][2]))
        graph[data[i][1]].append(Node(data[i][0], data[i][2]))

    heap = []

    # 1 -> V1 -> V2 -> END
    first_val = dijkstra(1, V1) + dijkstra(V1, V2) + dijkstra(V2, N)
    # 1 -> V2 -> V1 -> END
    second_val = dijkstra(1, V2) + dijkstra(V2, V1) + dijkstra(V1, N)

    result = min(first_val, second_val)
    print(-1 if result >= INF else result)
    
    