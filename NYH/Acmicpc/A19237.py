import sys

'''
    상어마다 빈칸을 찾는 
    특정한 우선순위가 있음
    shark_no : 상어 번호
    cur_d : 현재 상어의 방향
    shark_priority : 상어의 방향 우선순위 배열
    smell : 상어의 냄새 보드
'''

def input():
    return sys.stdin.readline().rstrip()

def shark_move(copy_board):
    for r in range(n):
        for c in range(n):
            if board[r][c] == 0:
                continue
            is_blank = False

            shark_no = copy_board[r][c]
            cur_d = shark_dir[shark_no]

            for i in range(4):
                # 현재 방향의 우선순위
                nd = shark_priority[shark_no][cur_d - 1][i]
                nr, nc = r + dirs[nd][0], c + dirs[nd][1]

                # 공간을 넘으면
                if nr < 0 or nr >=n or nc < 0 or nc >=n:
                    continue
                
                # 냄새가 없다면?
                if smell[nr][nc][1] == 0:

                    # 상어가 없다면?
                    if copy_board[nr][nc] == 0:
                        copy_board[nr][nc] = board[r][c]
                        copy_board[r][c] = 0

                    # 상어가 있다면?
                    else:
                        # 번호가 작은 상어가 이긴다.
                        if copy_board[nr][nc] > copy_board[r][c]:
                            copy_board[nr][nc] = board[r][c]
                        copy_board[r][c] = 0
                    shark_dir[shark_no] = nd

                    is_blank = True
                    break
            # 빈칸으로 이동한 경우
            if is_blank:
                continue

            # 냄새를 쫓아야 되는 경우
            for k in range(4):
                nd = shark_priority[shark_no][cur_d - 1][k]
                nr = r + dirs[nd][0]
                nc = c + dirs[nd][1]
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue

                if smell[nr][nc][1] == shark_no:
                    copy_board[nr][nc] = board[r][c]
                    copy_board[r][c] = 0
                    shark_dir[shark_no] = nd
                    break

    return copy_board

def smell_increase(k):
    for r in range(n):
        for c in range(n):
            if board[r][c] != 0:
                # 턴, 번호
                smell[r][c][0], smell[r][c][1] = k, board[r][c]

def smell_decrease():
    for r in range(n):
        for c in range(n):
            if smell[r][c][1] == 0:
                continue
            if smell[r][c][0] == 1:
                smell[r][c][0], smell[r][c][1] = 0, 0
            else:
                smell[r][c][0] -= 1

def check():
    is_check = False
    for r in range(n):
        for c in range(n):
            if board[r][c] > 1:
                return False
            elif board[r][c] == 1:
                is_check = True
            
    return True if is_check else False


if __name__=="__main__":
    n, m, k = map(int,input().split())
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    dirs = [[], (-1, 0), (1, 0), (0, -1), (0, 1)]

    # 초기 상어의 방향
    shark_dir = [0] + list(map(int, input().split()))
    '''
        shark_priority[n]

        현재 방향
        0 : 위
        1 : 아래
        2 : 왼쪽
        3 : 오른쪽
    '''
    shark_priority = [[] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for _ in range(4):
            p = list(map(int, input().split()))

            shark_priority[i].append(p)
        

    smell = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for time in range(1, 1001):
        copy_board = [item[:] for item in board]
        smell_increase(k)
        board = shark_move(copy_board)
        if check():
            print(time)
            exit()
        smell_decrease()


    print(-1)        


