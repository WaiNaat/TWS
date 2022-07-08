import sys
from itertools import combinations
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

if __name__ =="__main__":
    n, m = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(n)]

    virus_place = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == 2:
                virus_place.append((row, col))
                board[row][col] = 0
            elif board[row][col] == 0:
                board[row][col] = "[]"
            elif board[row][col] == 1:
                board[row][col] = "#"
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    min_time = 1e9

    
    for comp in combinations(virus_place, m):
        dec = deque()
        time = 0
        comp_board = [item[:] for item in board]
        is_False = False

        another = set(virus_place) - set(comp) 

        for c in comp:
            dec.appendleft(c)

        while dec:
            r, c = dec.pop()

            for dir in dirs:
                nr = r + dir[0]
                nc = c + dir[1]

                if nr < 0 or nr >=n or nc < 0 or nc >=n:
                    continue
                
                if comp_board[nr][nc] == "[]":
                    comp_board[nr][nc] = comp_board[r][c] + 1
                    dec.appendleft((nr, nc))
                if comp_board[nr][nc] == 0 and (nr, nc) in another:
                    comp_board[nr][nc] = comp_board[r][c] + 1
                    dec.appendleft((nr, nc))
                

        
        for row in range(n):
            for col in range(n):
                if comp_board[row][col] == "[]":
                    is_False = True
                    break

                elif comp_board[row][col] != "#" and (row, col) not in another  and comp_board[row][col] >= 1:
                    time = max(comp_board[row][col], time)

            if is_False:
                break
        
        if not is_False:
            min_time = min(time, min_time)
    
    if min_time == 1e9:
        print(-1)
    else:
        print(min_time)
