import sys

def input():
    return sys.stdin.readline().rstrip()


def move():
    global board
    m_board = [[[] for _ in range(C)] for _ in range(R)]
    dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for i in range(R):
        for j in range(C):
            if board[i][j]:
                r, c = i, j 
                w, d, s = board[i][j][0]

                s_cnt = s
                while s_cnt > 0:
                    nr = r + dirs[d][0]
                    nc = c + dirs[d][1]
                    
                    if nr < 0 or nr >= R or nc < 0 or nc >=C:
                        if d in [0, 2]:
                            d += 1
                        elif d in [1, 3]:
                            d -= 1
                    else:
                        r, c = nr, nc
                        s_cnt -= 1

                m_board[r][c].append([w, d, s])
    
    board = [item[:] for item in m_board]


if __name__=="__main__":
    R, C, M = map(int,input().split())
    board = [[[] for _ in range(C)] for _ in range(R)]
    for _ in range(M):
        r, c, s, d, w = map(int,input().split())

        board[r - 1][c - 1].append([w, d - 1, s])
    

    res = 0
    for fisher in range(C):

        for r in range(R):
            if board[r][fisher]:
                val = board[r][fisher][0]
                res += val[0]
                board[r][fisher].remove(val)
                break

        move()
    
        for i in range(R):
            for j in range(C):
                if len(board[i][j]) >= 2:
                    board[i][j].sort(reverse=True)
                    while len(board[i][j]) >=2:
                        board[i][j].pop()
    
    print(res)