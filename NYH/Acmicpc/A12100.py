import sys

def input():
    return sys.stdin.readline().rstrip()


def solution(cur_board):
    '''
        1. board 깊은 복사
        2. 한번 합쳐진 것은 다음 번 이동때 합칠 수 있음.
        3. 한번 합칠 때 이미 합친 것들은 합칠 수 없음.
        
    '''
    sub_ploblem(cur_board, cur_board, 0)
    return  

def top_move(board):
    global max_num

    for row in range(1, N):
        for col in range(N):
            
            x, y = row, col
            
            while x > 0 and board[x - 1][y] == 0:
                board[x - 1][y] = board[x][y]
                board[x][y] = 0
                x -= 1

    for row in range(1, N):
        for col in range(N):
            x, y = row, col
            if board[x][y] == 0:
                continue
            
            if board[x][y] == board[x - 1][y]:
                max_num = max(board[x - 1][y] * 2, max_num)
                board[x - 1][y] += board[x][y]
                board[x][y] = 0

    for row in range(1, N):
        for col in range(N):
            
            x, y = row, col

            if board[x][y] == 0:
                continue
            
            while x > 0 and board[x - 1][y] == 0:
                board[x - 1][y] = board[x][y]
                board[x][y] = 0
                x -= 1
            
    return board

def bottom_move(board):
    global max_num

    for row in range(N - 2, -1,  -1):
        for col in range(N):
            
            x, y = row, col

            if board[x][y] == 0:
                continue
            
            while x + 1 < N and board[x + 1][y] == 0:
                board[x + 1][y] = board[x][y]
                board[x][y] = 0
                x += 1

    for row in range(N - 2, -1,  -1):
        for col in range(N):
            x, y = row, col
            if board[x][y] == 0:
                continue
            
            if board[x][y] == board[x + 1][y]:

                max_num = max(board[x + 1][y] * 2, max_num)
                board[x + 1][y] += board[x][y]
                board[x][y] = 0


    for row in range(N - 2, -1,  -1):
        for col in range(N):
            
            x, y = row, col

            if board[x][y] == 0:
                continue
            
            while x + 1 < N and board[x + 1][y] == 0:
                board[x + 1][y] = board[x][y]
                board[x][y] = 0
                x += 1

    return board

def left_move(board):
    global max_num

    for row in range(N):
        for col in range(1, N):
            
            x, y = row, col

            if board[x][y] == 0:
                continue
            
            while y > 0 and board[x][y - 1] == 0:
                board[x][y - 1] = board[x][y]
                board[x][y] = 0
                y -= 1

    for row in range(N):
        for col in range(1, N):
            
            x, y = row, col
            if board[x][y] == 0:
                continue
            
            if board[x][y] == board[x][y - 1]:
                max_num = max(board[x][y - 1] * 2, max_num)
                board[x][y - 1] += board[x][y]
                board[x][y] = 0

    for row in range(N):
        for col in range(1, N):
            
            x, y = row, col

            if board[x][y] == 0:
                continue
            
            while y > 0 and board[x][y - 1] == 0:
                board[x][y - 1] = board[x][y]
                board[x][y] = 0
                y -= 1

    return board

def right_move(board):
    global max_num
    for row in range(N):
        for col in range(N - 2, -1,  -1):
            
            x, y = row, col
            if board[x][y] == 0:
                continue
            
            while y + 1 < N and board[x][y + 1] == 0:
                board[x][y + 1] = board[x][y]
                board[x][y] = 0
                y += 1

    # 2. 한번 합친다.
    for row in range(N):
        for col in range(N - 2, -1,  -1):
            
            x, y = row, col
            if board[x][y] == 0:
                continue

            if board[x][y] == board[x][y + 1]:
                # 합칠 때 한번 합친 블록은 또 합쳐지면 안된다.
                max_num = max(board[x][y + 1] * 2, max_num)
                board[x][y + 1] += board[x][y]
                board[x][y] = 0
                    
    for row in range(N):
        for col in range(N - 2, -1,  -1):
            
            x, y = row, col
            if board[x][y] == 0:
                continue
            
            while y + 1 < N and board[x][y + 1] == 0:
                board[x][y + 1] = board[x][y]
                board[x][y] = 0
                y += 1

    return board

def sub_ploblem(cur_board, prev_board, cnt):
    '''
        1. 이미 합쳐진 블록은 다시 합쳐지지 않는다.
        2. 똑같은 수가 세개가 있는 경우에는 
           이동하려고 하는 쪽의 칸이 먼저 합쳐진다.
        3. 이전 형태랑 board가 동일한 경우? => return
    '''
    if cnt == 5:
        return
    elif cnt > 0 and cur_board == prev_board:
        return
    else:

        # 이전 보드 형태 기억
        prev_board = [item[:] for item in cur_board]
        # 가져온 보드로 이동 하기 위한 복사
        board = [item[:] for item in prev_board]

        sub_ploblem(top_move(board), prev_board, cnt + 1)
        board = [item[:] for item in prev_board]

        sub_ploblem(bottom_move(board), prev_board, cnt + 1)
        board = [item[:] for item in prev_board]

        sub_ploblem(left_move(board), prev_board, cnt + 1)
        board = [item[:] for item in prev_board]

        sub_ploblem(right_move(board), prev_board, cnt + 1)
        board = [item[:] for item in prev_board]

    return

if __name__ =="__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
    for row in range(N):
        for col in range(N):
            if board[row][col] > max_num:
                max_num = board[row][col]
    solution(board)
    print(max_num)