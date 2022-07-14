import sys

'''
1번 행은 N번 행과 연결
1번 열은 N번 열과 연결
'''

def input():
    return sys.stdin.readline().rstrip()

def move_ball():
    g = [[[] for _ in range(n)]for _ in range(n)]
    # 이동
    for r in range(n):
        for c in range(n):
            if len(grid[r][c]) == 0:
                continue
            
            for fire in grid[r][c]:

                w, s, d = fire
                nr = (r + dirs[d][0] * s) % n
                nc = (c + dirs[d][1] * s) % n
                g[nr][nc].append([w, s, d])

    for r in range(n):
        for c in range(n):
            if len(g[r][c]) >= 2:
                fire_cnt = len(g[r][c])
                fire_dir = []
                w_sum, s_sum, is_odd_number, is_even_number = 0, 0, True, True

                for fire in g[r][c]:
                    w, s, d = fire
                    fire_dir.append(d)
                    w_sum += w
                    s_sum += s
                
                for d in fire_dir:

                    if d % 2 == 0:
                        is_odd_number = False
                    
                    elif d % 2 == 1:
                        is_even_number = False
                
                g[r][c] = []

                if w_sum // 5 > 0:
                    if is_odd_number or is_even_number:
                        for d in [0, 2, 4, 6]:
                            g[r][c].append([w_sum // 5, s_sum // fire_cnt, d])
                    else:
                        for d in [1, 3, 5, 7]:
                            g[r][c].append([w_sum // 5, s_sum // fire_cnt, d])
    return g

if __name__=="__main__":
    n, m, k = map(int, input().split())
    
    grid = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        # 행, 열, 무게, 속력, 방향
        r, c, w, s, d = map(int,input().split())
        grid[r - 1][c - 1].append([w, s, d])
    
    dirs = [
        (-1, 0), (-1, 1), (0, 1), (1, 1),
        (1, 0), (1, -1), (0, -1), (-1, -1)
    ]

    for _ in range(k):
        grid = move_ball()
    
    res = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c]:
                for fire in grid[r][c]:
                    res += fire[0]
    
    print(res)