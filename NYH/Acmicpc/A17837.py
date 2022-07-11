import sys
from collections import deque
'''
    0 : 흰색
    1 : 빨간색
    2 : 파란색

    흰색
    - 해당 칸으로 이동
    - 이동 칸에 말이 이미 있으면 
    그 말의 가장 위에 A번 말을 올려놓는다.
    - A번 말의 위에 다른 말이 있는 경우
        - A, B, C => D, E, A, B, C (D, E) 원래 있던 말
    
    빨간색
    - 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓인 순서를 반대로 바꿈
    - A, B, C 가 이동하고 이동 칸에 말이 없으면 C, B, A
    - A, D, F, G 가 이동하고 이동 칸에 E, C, B가 있으면
    - E, C, B, G, F, D, A
        말이 있는 경우
        순서를 뒤집고
        E, C, B를 앞에 붙인다.
        - G, F, D, A
        - E, C, B
    파란색
    - 말의 이동 방향을 반대로 하고 한 칸 이동
    - 방향을 반대로 바꾼 후에 이동 칸이 파란색이면
    이동하지 않고 가만히 있음.
    - 체스판을 벗어나는 경우는 파란색과 같음
        - 이동방향 변경
        - 파란색이면 가만히
        - 아니면 반대로 이동
    - 한 말이 이동시 위에 올려져 있는 말도 함께 이동
    
    한번 턴에 모든 체스말이 움직인다.
'''
    

def input():
    return sys.stdin.readline().rstrip()

def change_dir(d):
    # 방향 변경
    if d in [1, 3]:
        d += 1
    elif d in [2, 4]:
        d -= 1
    return d

def check(r, c):
    if len(chess[r][c]) >= 4:
        return True
    return False

def white(no, r, c, nr, nc):
    # 해당 칸부터 위까지 삭제.
    for idx in range(chess[r][c].index(no), len(chess[r][c])):
        # 다음 칸에 추가
        chess[nr][nc].append(chess[r][c][idx])
        horses[chess[r][c][idx]][0], horses[chess[r][c][idx]][1] = nr, nc
    
    for _ in range(chess[r][c].index(no), len(chess[r][c])):
        chess[r][c].pop()


def red(no, r, c, nr, nc):
    # 해당 칸부터 위까지 삭제.
    for idx in range(len(chess[r][c]) - 1, chess[r][c].index(no) -1, -1):
        # 다음 칸에 추가
        chess[nr][nc].append(chess[r][c][idx])
        horses[chess[r][c][idx]][0], horses[chess[r][c][idx]][1] = nr, nc
    
    for _ in range(chess[r][c].index(no), len(chess[r][c])):
        chess[r][c].pop()

if __name__=="__main__":
    n, k = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    chess = [[deque() for _ in range(n)] for _ in range(n)]

    horses = []
    for i in range(k):
        r, c, d = map(int, input().split())
        horses.append([r - 1, c - 1, d])
        chess[r - 1][c - 1].append(i)
    
    dirs = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]

    cnt = 1
    is_break = False
    while True:

        if cnt == 1000:
            print(-1)
            break
        
        for no in range(k):
            r, c, d = horses[no]
            nr, nc = r + dirs[d][0], c + dirs[d][1]

            # 파란색이거나 공간을 넘는다면?
            if (nr < 0 or nr >= n or nc < 0 or nc >=n) or board[nr][nc] == 2:
                d = change_dir(d)
                horses[no][2] = d

                nr, nc = r + dirs[d][0], c + dirs[d][1]
                if (nr < 0 or nr >= n or nc < 0 or nc >=n) or board[nr][nc] == 2:
                    continue

                elif board[nr][nc] == 0:
                    white(no, r, c, nr, nc)
                    if check(nr, nc):
                        print(cnt)
                        exit()

                elif board[nr][nc] == 1:
                    red(no, r, c, nr, nc)
                    if check(nr, nc):
                        print(cnt)
                        exit()

            # 흰색 이라면?
            elif board[nr][nc] == 0:
                white(no, r, c, nr, nc)
                if check(nr, nc):
                    print(cnt)
                    exit()
                
            # 빨간색 이라면?
            elif board[nr][nc] == 1:
                red(no, r, c, nr, nc)
                if check(nr, nc):
                    print(cnt)
                    exit()
        cnt += 1
            