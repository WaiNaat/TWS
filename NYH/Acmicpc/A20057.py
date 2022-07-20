import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def tornado(pos, dir, cur_sand):
    global _out
    '''
        dir : 방향
        pos : 현재 위치
        1. 보드의 모래를 이동시킨다.
        2. 흩날린 양을 반환한다.

        pos가 (0, 0)이면 종료한다.
        dir은 1씩 더하면서 % 4 해준다.
        모래가 이미 있는 칸으로 모래가 이동하면, 
        모래의 양은 더해진다.

    '''
    r, c = pos
    f_board = tornado_board[dir]

    
    a_r, a_c = -1, -1
    sand = 0
    for i in range(-2, 3):
        for j in range(-2, 3):
            nr, nc = r + i, c + j
            x, y = i + 2, j + 2
            if f_board[x][y] == 0 or f_board[x][y] == -1:
                if f_board[x][y] == -1:
                    a_r, a_c = r + i, c + j
                continue

            val = int(cur_sand * (f_board[x][y]) / 100)
            sand += val

            # 범위에 속하면?
            if nr < 0 or nr >=n or nc < 0 or nc >=n:
                _out += val
            else:
                board[nr][nc] += val
                

    # 이동 방향에 존재하는 칸.
    if 0 <= a_r < n and 0 <= a_c < n:
        board[a_r][a_c] += (cur_sand - sand)
    else:
        _out += (cur_sand - sand)
    
    

if __name__=="__main__":
    n = int(input())

    board = [list(map(int,input().split())) for _ in range(n)]
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    tornado_board = [
        # left
        [[0,0,2,0,0],[0,10,7,1,0],[5,-1,0,0,0],[0,10,7,1,0],[0,0,2,0,0]],
        # down
        [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,-1,10,0],[0,0,5,0,0]],
        # right
        [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,-1,5],[0,1,7,10,0],[0,0,2,0,0]],
        # up
        [[0,0,5,0,0],[0,10,-1,10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]],
    ]
        
    '''
        토네이도 길이
        1, 1
        2, 2
        ... n - 1, n - 1

        토네이도에서 사용되는 모든 좌표 값을 미리 계산.
    '''

    # 시작 좌표
    s_r, s_c = n // 2, n // 2

    # (0, 0 도달 전까지)
    _out = 0

    # 초기 방향
    d = 0

    tor_pos = []
    len_cnt = 0
    len_tor = 1
    
    pos = deque([[s_r, s_c, d]])
    while pos:
        r, c, dir = pos.pop()
        

        if len_cnt !=0 and len_cnt %2 == 0:
            len_tor += 1
        
        for _ in range(len_tor):
            nr, nc = r + dirs[dir][0], c + dirs[dir][1]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            r, c = nr, nc
            tor_pos.append((nr, nc, dir))
        
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        
        dir += 1
        dir = dir % 4
        pos.appendleft([nr, nc, dir])            
        

        len_cnt += 1

    for tor in tor_pos:
        r, c, d = tor
        tornado((r, c), d, board[r][c])
        board[r][c] = 0
    
    print(_out)






    




        
        
    