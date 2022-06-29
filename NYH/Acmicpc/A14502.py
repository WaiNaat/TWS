import sys
from collections import deque
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def solution():
    global max_zero
    '''
    1. 비어 있는 공간에서 랜덤으로 3개 세운다.
    2. 바이러스 2를 bfs해서 퍼뜨린다.
    3. 남아있는 0을 센다.
    '''
    for comb in list(combinations(zero_place, 3)):
        max_zero = max(sub_ploblem(comb), max_zero)

def sub_ploblem(comb):
    global board
    # 원본 보드 복구    
    prev_board = [item[:] for item in board]

    for idx in comb:
        x, y = idx
        board[x][y] = 1

    queue = deque(virus_place)
    

    while queue:

        x, y = queue.pop()

        for dir in dirs:
            dx, dy = x + dir[0], y + dir[1]

            if dx < 0 or dx >= N or dy < 0 or dy >= M:
                continue
            
            if board[dx][dy] == 1 or board[dx][dy] == 2:
                continue
            
            # 바이러스 전파
            if board[dx][dy] == 0:
                queue.appendleft((dx, dy))
                board[dx][dy] = 2

    cnt = 0

    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                cnt += 1

    board = [item[:] for item in prev_board]

    return cnt

if __name__=="__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_zero = 0
    zero_place = []
    virus_place = []
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                zero_place.append((row, col))
            if board[row][col] == 2:
                virus_place.append((row, col))
    
    solution()
    print(max_zero)