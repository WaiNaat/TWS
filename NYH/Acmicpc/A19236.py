import sys
import copy
'''
    상어는 0, 0 의 물고기 방향
    물고기는 한번에 한칸 이동
    - 다른 물고기 있는 칸, 빈 칸
    - 이동 시 해당 위치의 물고기와 자리를 바꾼다.
    이동 불가능한 칸
    - 상어가 있는 칸, 공간의 경계를 넘는 칸

    상어의 이동
    - 물고기를 먹을 때마다 방향을 갖게 되고
    방향이 목적지에 도달했을 때 물고기를 먹고
    해당 물고기의 방향을 다시 갖게 된다.
    - 
'''
def input():
    return sys.stdin.readline().rstrip()


def dfs(score, board):
    global max_score
    global shark

    r, c, d = shark
    move_fish(board)
    shark_pos = shark_space(r, c, d, board)
    max_score = max(score, max_score)

    # 이동할 곳이 없으면?
    if not shark_pos:
        return

    for m_shark in shark_pos:
        prev_board = copy.deepcopy(board)
        # 이동 및 식사
        nr, nc, nd, no = m_shark
        shark = [nr, nc, nd]

        # 먹은 표시
        
        board[nr][nc][0] = -1
        eat_fish[no] = True
        dfs(score + no, board)
        board = prev_board
        eat_fish[no] = False
        shark = [r, c, d]
        

    return

def shark_space(r, c, d, board):
    move_shark = []
    nr, nc = r, c
    while (0 <= nr < 4 and 0 <= nc < 4):
        nr, nc = nr + dirs[d][0], nc + dirs[d][1]
        
        # 공간을 벗어나지 않고 먹히지 않은 상황인 경우?
        # 잡아먹히면 공간을 비운다.
        if (0 <= nr < 4 and 0 <= nc < 4) and board[nr][nc][0] > 0 :
            no, nd = board[nr][nc]
            move_shark.append([nr, nc, nd, no])

    return move_shark

def move_fish(board):
    # fish 배열에서 1번부터 순서대로 움직인다.

    shark_r, shark_c = shark[0], shark[1]
    for no in range(1, 17):
        
        # 상어한테 먹히지 않은 물고기만 움직인다.
        if not eat_fish[no]:
            is_fish = False
            for r in range(4):
                for c in range(4):
                    if board[r][c][0] == no:
                        is_fish = True
                        break

                if is_fish:
                    break
            
            d = board[r][c][1]

            for j in range(8):
                nd = (d + j) % 9
                if nd == 0:
                    nd = 1

                nr, nc = r + dirs[nd][0], c + dirs[nd][1]

                # 공간을 넘으면?, 상어가 있으면?
                if (nr < 0 or nr >= 4 or nc < 0 or nc >=4) or (nr == shark_r and nc == shark_c):
                    continue
                
                # 물고기가 있든 없든 위치 교환
                board[r][c][1] = nd
                swap_fish(board, r, c, nr, nc)
                break
                

def swap_fish(board, r, c, nr, nc):
    temp = board[r][c]
    board[r][c] = board[nr][nc]
    board[nr][nc] = temp


if __name__=="__main__":
    dirs = [
        (), (-1, 0), (-1, -1), (0, -1), (1, -1),
        (1, 0), (1, 1), (0, 1), (-1, 1)
    ]

    b = [[] for _ in range(4)]
    for i in range(4):
        _list = list(map(int, input().split()))
        b[i] = [[_list[j * 2]  , _list[j * 2 + 1] ] for j in range(4)] 

    score = b[0][0][0]

    shark = [0, 0, b[0][0][1]]
    eat_fish = [False for _ in range(17)]

    # 0, 0의 물고기는 먹힌 상태로 시작.
    eat_fish[b[0][0][0]] = True
    max_score = score
    b[0][0][0] = -1

    dfs(score, b)
    print(max_score)

