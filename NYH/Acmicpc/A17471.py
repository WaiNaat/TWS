import sys
from itertools import combinations
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def possible(comb1, comb2):

    c1, c2 = True, True

    if len(comb1) >= 2:
        for node in comb1:

            targets = [num for num in comb1]
            targets.remove(node)
            if not bfs(node, targets):
                c1 = False
    
    if len(comb2) >= 2:
        for node in comb2:
            targets = [num for num in comb2]
            targets.remove(node)
            if not bfs(node, targets):
                c2 = False

    if c1 and c2:
        return True    
    else:
        return False

def bfs(node, targets):
    '''
        해당 node에서
        comb에 해당하는 모든 노드가 visited True 인가?
    '''
    
    visited = [False for _ in range(n + 1)]
    visited[node] = True
    q = deque([node])

    while q:
        cur = q.pop()

        for loc in location[cur]:
            if not visited[loc] and loc in targets:
                visited[loc] = True
                q.appendleft(loc)

    for target in targets:
        if not visited[target]:
            return False


    return True

if __name__=="__main__":
    INF = 1e9
    '''
        0 : 2 4 (2)
        1 : 1 3 6 5 (4)
        2 : 4 2 (2)
        3 : 1 3 (2)
        4 : 2 (1)
        5 : 2 (1)

    그래프에서 두개의 선거구로 
    나눌 수 있는 경우의 수를 구한다.
    '''
    n = int(input())
    population = [0] + list(map(int, input().split()))
    
    location = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        near_location  = list(map(int, input().split()))
        location[i] = near_location[1:]
    
    res = INF
    
    '''
        선거구간 노드 숫자를 정한다.
        ex)
        1, 6
            1개의 노드를 7개 중에 선택
        2, 5
            2개의 노드를 7개 중에 선택
        3, 4
            3개의 노드를 7개 중에 선택
    '''

    numbers = []
    case = [i for i in range(1, n + 1)]
    for i in range(1, n // 2 + 1):
        numbers.append(i)

    for num in numbers:

        for comb1 in combinations(case, num):
            comb2 = list(set(case) - set(comb1))
            
            if possible(list(comb1), comb2):
                left_val, right_val = 0, 0
                for idx in comb1:
                    left_val += population[idx]
                for idx in comb2:
                    right_val += population[idx]
                
                res = min(res, abs(left_val - right_val))
    print(-1 if res == INF else res)
