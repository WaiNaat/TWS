import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def solution(N, M, board):

    '''
    1. M개의 치킨 조합 구하기
    2. 조합 마다 치킨 거리 구하기
    3. 최적의 치킨 거리 갱신.
    '''
    INF = 1e9
    chicken = []
    house = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                chicken.append((i, j))
            if board[i][j] == 1:
                house.append((i, j))

    min_list = []
    for comb in combinations(chicken, M):
        distance = [INF] * len(house)
        for x, y in comb:
            distance = sub_ploblem(x, y, house, distance)
        min_list.append(sum(distance))
    return min(min_list)

def sub_ploblem(c_x, c_y, house, distance):
    '''
        치킨 거리 갱신 => 각 집마다 해당 조합에서의 최소 거리 반환.
    '''

    idx = 0
    for home in house:
        h_x, h_y = home
        distance[idx] = min(abs(c_x - h_x) + abs(c_y - h_y), distance[idx])
        idx += 1
    
    return distance


if __name__=="__main__":
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    print(solution(N, M, board))