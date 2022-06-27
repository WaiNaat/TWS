import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution(row, col):
    global board
    '''
        실패 조건
        1. 파란 구슬이 구멍에 빠진다.
        2. 빨간 구슬과 파란 구슬이 동시에 구멍에 빠진다.
        3. 파란 구슬과 빨간 구슬은 동시에 같은 칸에 움직일 수 없다.
        4. 10번 이상 움직이면 -1
        O는 구멍 위치 #은 벽, R은 빨간B 구슬, 는 파란 구슬, .은 비어있다.
        한번 기울일때 벽에 닿을때까지 움직인다.
        상태는 총 3가지 경우가 있다.
    '''
    
    blue = ()
    red = ()
    for i in range(row):
        for j in range(col):
            if board[i][j] == "B":
                blue = (i, j)
            elif board[i][j] == "R":
                red = (i, j)
            
    queue = deque()
    queue.append([red, blue, 0])

    while queue:
        '''
            0 queue에 넣을 수 있는 상태
            1 성공한 상태
            2 queue에 넣을 수 없는 상태(실패)
            board의 R과 B가 계속 변경되는 점을 고려해야함.
        '''
        red_ball, blue_ball, cnt = queue.pop()

        if cnt >= 10:
            return -1
        
        red_x, red_y = red_ball
        blue_x, blue_y = blue_ball
        board[red_x][red_y] = "R"
        board[blue_x][blue_y] = "B"

        prev_board = [item[:] for item in board]

        left_obj = left_move(blue_x, blue_y, red_x, red_y)
        if left_obj[2] == 0 and (left_obj[0] != red_ball or left_obj[1] != blue_ball):
            # 이동이 있는 경우
            queue.appendleft((left_obj[0], left_obj[1], cnt + 1))

        elif left_obj[2] == 1:
            return cnt + 1

        board = [item[:] for item in prev_board]

        right_obj = right_move(blue_x, blue_y, red_x, red_y)
        if right_obj[2] == 0 and (right_obj[0] != red_ball or right_obj[1] != blue_ball):
            queue.appendleft((right_obj[0], right_obj[1], cnt + 1))
        elif right_obj[2] == 1:
            return cnt + 1

        board = [item[:] for item in prev_board]

        top_obj = top_move(blue_x, blue_y, red_x, red_y)
        if top_obj[2] == 0 and (top_obj[0] != red_ball or top_obj[1] != blue_ball):
            queue.appendleft((top_obj[0], top_obj[1], cnt + 1))
        elif top_obj[2] == 1:
            return cnt + 1

        board = [item[:] for item in prev_board]
        
        bottom_obj = bottom_move(blue_x, blue_y, red_x, red_y)
        if bottom_obj[2] == 0 and (bottom_obj[0] != red_ball or bottom_obj[1] != blue_ball):
            queue.appendleft((bottom_obj[0], bottom_obj[1], cnt + 1))    
        elif bottom_obj[2] == 1:
            return cnt + 1
        
        board = [item[:] for item in prev_board]

        board[red_x][red_y] = "."
        board[blue_x][blue_y] = "."

    return -1

def left_move(blue_x, blue_y, red_x, red_y):
    val = 0
    while board[red_x][red_y - 1] == ".":
        board[red_x][red_y] = "."
        red_y -= 1
        board[red_x][red_y] = "R"
        
    
    if board[red_x][red_y - 1] == "O":
        val = 1
        board[red_x][red_y] = "."

    while board[blue_x][blue_y - 1] == ".":
        board[blue_x][blue_y] = "."
        blue_y -= 1
        board[blue_x][blue_y] = "B"

    if board[blue_x][blue_y - 1] == "O":
        val = 2
        board[blue_x][blue_y] = "."
    
    while board[red_x][red_y - 1] == ".":
        board[red_x][red_y] = "."
        red_y -= 1 
        board[red_x][red_y] = "R"

    return [(red_x, red_y), (blue_x, blue_y), val]

def right_move(blue_x, blue_y, red_x, red_y):
    val = 0

    while board[red_x][red_y + 1] == ".":
        board[red_x][red_y] = "."
        red_y += 1
        board[red_x][red_y] = "R"
        
    
    if board[red_x][red_y + 1] == "O":
        val = 1
        board[red_x][red_y] = "."

    while board[blue_x][blue_y + 1] == ".":
        board[blue_x][blue_y] = "."
        blue_y += 1
        board[blue_x][blue_y] = "B"

    
    if board[blue_x][blue_y + 1] == "O":
        val = 2
        board[blue_x][blue_y] = "."
    
    while board[red_x][red_y + 1] == ".":
        board[red_x][red_y] = "."
        red_y += 1
        board[red_x][red_y] = "R"

    return [(red_x, red_y), (blue_x, blue_y), val]

def top_move (blue_x, blue_y, red_x, red_y):
    val = 0

    while board[red_x - 1][red_y] == ".":
        board[red_x][red_y] = "."
        red_x -= 1
        board[red_x][red_y] = "R"
        
    
    if board[red_x - 1][red_y] == "O":
        val = 1
        board[red_x][red_y] = "."

    while board[blue_x - 1][blue_y] == ".":
        board[blue_x][blue_y] = "."
        blue_x -= 1
        board[blue_x][blue_y] = "B"

    
    if board[blue_x - 1][blue_y] == "O":
        val = 2
        board[blue_x][blue_y] = "."
    
    while board[red_x - 1][red_y] == ".":
        board[red_x][red_y] = "."
        red_x -= 1
        board[red_x][red_y] = "R"

    return [(red_x, red_y), (blue_x, blue_y), val]

def bottom_move(blue_x, blue_y, red_x, red_y):
    val = 0

    while board[red_x + 1][red_y] == ".":
        board[red_x][red_y] = "."
        red_x += 1
        board[red_x][red_y] = "R"
        
    
    if board[red_x + 1][red_y] == "O":
        val = 1
        board[red_x][red_y] = "."

    while board[blue_x + 1][blue_y] == ".":
        board[blue_x][blue_y] = "."
        blue_x += 1
        board[blue_x][blue_y] = "B"

    
    if board[blue_x + 1][blue_y] == "O":
        val = 2
        board[blue_x][blue_y] = "."
    
    while board[red_x + 1][red_y] == ".":
        board[red_x][red_y] = "."
        red_x += 1
        board[red_x][red_y] = "R"

    return [(red_x, red_y), (blue_x, blue_y), val]


if __name__=="__main__":
    N, M = map(int,input().split())
    board = [list(map(str, input())) for _ in range(N)]
    print(solution(N, M))