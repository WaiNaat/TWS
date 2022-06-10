import sys
import heapq

'''
    시작점에서 g - h 사이의 교차로를 무조건 지나므로
    s -> g -> h -> end
    s -> h -> g -> end
    의 경우의 수에서 최단 거리를 구하면 된다.
    다만 이 때 g와 h를 지나는 경로가 목적지로 향하는 최단 경로가 아닌 경우 해답에서 제외한다.
'''

INF = 1e9
def input():
    return sys.stdin.readline().rstrip()

def solution():
    T = int(input())
    result_list = [[] for _ in range(T)]
    cnt = 0
    for _ in range(T):
        n, m, t = map(int,input().split())
        s, g, h = map(int,input().split())
        graph = [[] for _ in range(n + 1)]

        destination = []
        for _ in range(m):
            a, b, d = map(int,input().split())
            graph[a].append((b, d))
            graph[b].append((a, d))

        for _ in range(t):
            destination.append(int(input()))
        
        result_list[cnt] = sub_ploblem(s, g, h, graph, destination, n)
        cnt += 1
    
    for result in result_list:
        print(" ".join(map(str, result)))



def sub_ploblem(s, g, h, graph, destination, node):

    result = []

    for dest in destination:
        min_case = dijkstra(s, dest, node, graph)
        g_to_h = dijkstra(g, h, node, graph)

        case_1 = dijkstra(s, g, node, graph)
        case_1 += g_to_h
        case_1 += dijkstra(h, dest, node, graph)

        case_2 = dijkstra(s, h, node, graph)
        case_2 += g_to_h
        case_2 += dijkstra(g, dest, node, graph)

        if case_1 == min_case or case_2 == min_case:
            result.append(dest)

    result.sort()

    return result

def dijkstra(start, end, node, graph):
    dist = [INF] * (node + 1)
    dist[start] = 0
    heap = []

    # weight, to
    heapq.heappush(heap, (0, start))

    while heap:
        cur_weight, to_node = heapq.heappop(heap)
        
        if dist[to_node] < cur_weight:
            continue
        
        for adj_to, adj_weight in graph[to_node]:
            if dist[adj_to] > cur_weight + adj_weight:
                dist[adj_to] = cur_weight + adj_weight
                heapq.heappush(heap, (dist[adj_to], adj_to))

    return dist[end]



if __name__ == "__main__":
    solution()