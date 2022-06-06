import sys
import heapq


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


def solution():
    INF = 1e9
    V, E = map(int, input().split())
    S = int(input())

    data = [list(map(int, input().split())) for _ in range(E)]
    heap = []
    dist = [INF] * (V + 1)

    
    
    graph = [[0] for _ in range(V + 1)]

    for i in range(len(data)):
        graph[data[i][0]].append(Node(data[i][1], data[i][2]))

    # 시작 노드 0 으로 초기화
    dist[S] = 0

    # 시작점 기입
    heapq.heappush(heap, Node(S, 0))

    # heap이 비어있지 않은 동안 수행
    while heap:
        curNode = heapq.heappop(heap)

        # 현재 노드가 가리키는 방향까지의 최소값이 curNode의 
        # weight 값보다 작으면 업데이트 필요성이 없음
        if dist[curNode.to] < curNode.weight:
            continue
        
        for i in range(1, len(graph[curNode.to])):
            add_node = graph[curNode.to][i]
            if dist[add_node.to] > curNode.weight + add_node.weight:
                dist[add_node.to] = curNode.weight + add_node.weight
                heapq.heappush(heap, Node(add_node.to, dist[add_node.to]))
    
    for i in range(1, len(dist)):
        if dist[i] == INF:
            print("INF")
        else:
            print(dist[i])


if __name__ == "__main__":
    solution()