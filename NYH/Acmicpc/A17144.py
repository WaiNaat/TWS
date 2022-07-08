import sys
'''
    A(r,c) = A - (A(r, c) // 5 ) * dir
    1. 확산
    2. 청소
'''
def input():
    return sys.stdin.readline().rstrip()

if __name__=="__main__":
    R, C, T = map(int,input().split())
    board = [list(map(int,input().split())) for _ in range(R)]

    air_cleaner = []
    for row in range(R):
        if board[row][0] == -1:
            air_cleaner.append((row, 0))
    
    u_row = air_cleaner[0][0]
    d_row = air_cleaner[1][0]

    dirs = [(0, 1), (0, -1),(1, 0), (-1, 0)]

    res = 0
    for _ in range(T):
        dusts = []
        # 매초 마다 동시에 먼지 확산
        for row in range(R):
            for col in range(C):
                if board[row][col] > 0:
                    dusts.append((row, col, board[row][col]))
        
        for dust in dusts:
            r, c, w = dust
            diff = w // 5
            
            diff_dirs = []
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]

                if nr < 0 or nr >= R or nc < 0 or nc >= C:
                    continue

                if (nr, nc) in air_cleaner:
                    continue
                
                diff_dirs.append((nr, nc))

            for diff_dir in diff_dirs:
                dr, dc = diff_dir
                board[dr][dc] += diff

            board[r][c] -= diff * len(diff_dirs)
        
        
        # 위
        
        # 위쪽 공기청정기 흡수
        board[u_row - 1][0] = 0

        # 1
        for r in range(u_row - 2, -1, -1):
            board[r + 1][0] = board[r][0]

        # 2
        for c in range(1, C):
            board[0][c - 1] = board[0][c]
        # 3
        for r in range(1, u_row + 1):
            board[r - 1][C - 1] = board[r][C - 1]
        # 4       
        for c in range(C - 2, 0, - 1):
            board[u_row][c + 1] = board[u_row][c]

        board[u_row][1] = 0

        # 아래

        # 아랫 부분 흡수
        board[d_row + 1][0] = 0

        # 1
        for r in range(d_row + 2, R):
            board[r - 1][0] = board[r][0]
        
        # 2
        for c in range(1, C):
            board[R - 1][c - 1] = board[R - 1][c]
        
        # 3
        for r in range(R - 2, d_row - 1, -1):
            board[r + 1][C - 1] = board[r][C - 1]

        # 4      
        for c in range(C - 2, 0, - 1):
            board[d_row][c + 1] = board[d_row][c]

        board[d_row][1] = 0
        
        

    for row in range(R):
        for col in range(C):
            if board[row][col] > 0:
                res += board[row][col]

    print(res)

        