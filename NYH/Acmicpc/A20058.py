import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def rotate(array):
    rotate_arr = zip(*array[::-1])
    return [list(val) for val in rotate_arr]


def move(level):

    # 시작 행, 열
    s_r, s_c = 0, 0

    # 회전
    while s_r < n:
        tile = [[0 for _ in range(level)] for _ in range(level)]

        for i in range(level):
            for j in range(level):
                tile[i][j] = grid[s_r + i][s_c + j]
        
        g = rotate(tile)

        for i in range(level):
            for j in range(level):
                grid[s_r + i][s_c + j] = g[i][j]

        s_c += level

        if s_c >= n:
            s_c = 0
            s_r += level

def decrease_ice():

    decrease_arr = []

    for r in range(n):
        for c in range(n):
            _cnt = 0

            # 얼음이 아닌 구역은 무시한다.
            if grid[r][c] == 0:
                continue

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    continue
                
                if grid[nr][nc] > 0:
                    _cnt += 1

            if _cnt < 3:
                decrease_arr.append((r, c))

    for pos in decrease_arr:
        r, c = pos
        grid[r][c] -= 1


def search_ice(r, c):
    size = 1
    queue = deque([[r, c]])
    

    while queue:
        r, c = queue.pop()

        visited[r][c] = True

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or nr >=n or nc < 0 or nc >=n:
                continue

            elif not visited[nr][nc] and grid[nr][nc] > 0:
                # 방문하지 않았고 얼음이라면?
                queue.appendleft((nr, nc))
                visited[nr][nc] = True
                size += 1
    
    return size

if __name__ =="__main__":
    n, q = map(int, input().split())
    n = 2 ** n

    grid = [list(map(int, input().split())) for _ in range(n)]
    '''
        덩어리 : 얼음이 있는 칸과 얼음이 있는칸끼리 연결된 집합
    '''
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    l = list(map(int, input().split()))
    for i in range(len(l)):
        v = l[i] 
        l[i] = 2 ** v

    # 이동
    for val in l:
        move(val)
        decrease_ice()
    
    # 얼음 합 구하기
    # 얼음 덩어리 칸 개수 구하기.
    sum_ice = 0
    max_size = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            sum_ice += grid[r][c]
            if grid[r][c] > 0 and not visited[r][c]:
                max_size = max(search_ice(r, c), max_size)

    print(sum_ice)
    print(max_size)


        

