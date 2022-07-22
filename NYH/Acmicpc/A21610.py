import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def move(order, clouds):
    d, s = order

    add_water = deque()
    
    while clouds:
        r, c = clouds.pop()

        # 1번 행과 n번 행이 연결됨, 
        # 마찬 가지로 1번 열과 n번 열도 연결
        for _ in range(s):
            nr = (r + dr[d] + n) % n
            nc = (c + dc[d] + n) % n
            r, c = nr, nc


        # 각 구름에서 비가 내려 구름이 있는 칸의 
        # 바구니에 저장된 물의 양이 1 증가.
        grid[nr][nc] += 1

        add_water.appendleft((nr, nc))
    
    save_clouds = list(add_water)

    while add_water:
        r, c = add_water.pop()
        
        lt_nr, lt_nc = r + dr[2], c + dc[2]
        ld_nr, ld_nc = r + dr[8], c + dc[8]
        rt_nr, rt_nc = r + dr[4], c + dc[4]
        rd_nr, rd_nc = r + dr[6], c + dc[6]

        _cnt = 0

        if 0 <= lt_nr < n and 0 <= lt_nc < n and grid[lt_nr][lt_nc] > 0:
            _cnt += 1
        
        if 0 <= ld_nr < n and 0 <= ld_nc < n and grid[ld_nr][ld_nc] > 0:
            _cnt += 1

        if 0 <= rt_nr < n and 0 <= rt_nc < n and grid[rt_nr][rt_nc] > 0:
            _cnt += 1

        if 0 <= rd_nr < n and 0 <= rd_nc < n and grid[rd_nr][rd_nc] > 0:
            _cnt += 1
        

        grid[r][c] += _cnt
    

    clouds = []    
    for r in range(n):
        for c in range(n):
            if grid[r][c] >= 2 and (r, c) not in save_clouds:
                clouds.append([r, c])
                grid[r][c] -= 2


        

    return clouds

if __name__ =="__main__":
    '''
    (n - 1, 1), (n - 1 , 2), (n - 2, 1), (n - 2, 2)

    (n - 1, n - 1) 인접 대각선 (n - 2, n - 2)
    경계를 넘어가면 안됨.
    '''

    dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

    n, m = map(int, input().split())

    grid = [list(map(int,input().split())) for _ in range(n)]
    
    move_order = []
    for _ in range(m):
        d, s = map(int, input().split())
        move_order.append((d, s))
    
    clouds = [(n - 1, 0), (n - 1 , 1), (n - 2, 0), (n - 2, 1)]

    for i in range(m):
        clouds = move(move_order[i], clouds)
    
    res = 0
    for r in range(n):
        for c in range(n):
            res += grid[r][c]
    print(res)