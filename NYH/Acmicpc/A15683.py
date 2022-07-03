import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def solution(cameras, board, N, M):
    '''
        0 빈칸
        6 벽
        감시 가능한 영역 "#"
    '''

    cctv = deque()
    for row in range(N):
        for col in range(M):
            if board[row][col] >= 1 and board[row][col] <= 5:
                cctv.appendleft((row, col, board[row][col]))

    sub_ploblem(0, cameras, cctv, board)
    return

def sub_ploblem(depth, cameras, cctv, board):
    global blind_spot
    if len(cctv) == depth:
        cnt = 0
        for i in range(len(board)):
            cnt += board[i].count(0)
        blind_spot = min(blind_spot, cnt)
        return
    
    compare_board = [item[:] for item in board]
    x, y, num = cctv[depth]
    for d in cameras[num]:
        fill_board(x, y, d, compare_board)
        sub_ploblem(depth + 1, cameras, cctv, compare_board)
        compare_board = [item[:] for item in board]

    return


def fill_board(x, y, d, board):
    for dir in d:
        nx = x
        ny = y
        while True:
            nx += dirs[dir][0]
            ny += dirs[dir][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if board[nx][ny] == 6:
                break
            elif board[nx][ny] == 0:
                board[nx][ny] = "#"
    return

if __name__=="__main__":
    '''
        1번 검증 dirs 전부
        2번 검증 (0, 1), (0, -1) / (1, 0), (-1, 0)
        3번 검증 
        - (0, 1), (1, 0)
        - (0, 1), (-1, 0)
        - (0, -1), (1, 0)
        - (0, -1), (-1, 0)
        4번 검증 
        - (0, 1), (0, -1), (1, 0)
        - (0, 1), (0, -1), (-1, 0)
        - (0, -1), (1, 0), (-1, 0)
        - (0, 1), (1, 0), (-1, 0)

        5번 검증
        - (0, 1), (0, -1),(1, 0), (-1, 0)
    '''
    dirs = [(0, 1), (0, -1),(1, 0), (-1, 0)]
    cameras = [
        [], 
        [[0], [1], [2], [3]],
        [[0, 1], [2, 3]],
        [
            [0, 2], [0, 3],
            [1, 2], [1, 3]
        ],

        [
            [0, 1, 2],
            [0, 1, 3],
            [0, 2, 3],
            [1, 2, 3]
        ],

        [[0, 1, 2, 3]]
    ]
    
    N, M = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(N)]
    blind_spot = 1e9
    solution(cameras, board, N, M)
    print(blind_spot)