import sys
import copy

def input():
    return sys.stdin.readline().rstrip()

def calc(g):
    global n
    min_val = 1e9

    for r in range(n):
        min_val = min(sum(g[r]), min_val)


    return min_val

def dfs(cnt, g):
    global k, res

    if cnt == k:
        res = min(res, calc(g))
        return
    
    for i in range(k):
        if not visited[i]:
            visited[i] = True
            board = rotate(rotate_array[i][0], rotate_array[i][1], copy.deepcopy(g))
            dfs(cnt + 1, board)
            visited[i] = False

    return

def rotate(dot1, dot2, g):
    '''

    '''
    r1, c1 = dot1
    r2, c2 = dot2
    
    while (r1, c1) != (r2, c2):
        temp = g[r1][c1]
        # 왼쪽
        for i in range(r1, r2):
            g[i][c1] = g[i + 1][c1]
        
        # 아래
        for i in range(c1, c2):
            g[r2][i] = g[r2][i + 1]
        
        # 오른쪽 위부터 아래로
        for i in range(r2, r1, -1):
            g[i][c2] = g[i - 1][c2]

        # 왼쪽 위 부터 오른쪽으로
        for i in range(c2, c1, -1):
            g[r1][i] = g[r1][i - 1]
        
        g[r1][c1 + 1] = temp

        r1 += 1
        c1 += 1
        r2 -= 1
        c2 -= 1
    return g

if __name__=="__main__":
    '''

        (r, c, s)
        (r - s, c - s)
        (r + s, c - s) 사각형 회전    
    '''
    n, m, k = map(int, input().split())
    res = 1e9
    grid = [list(map(int, input().split())) for _ in range(n)]
    rotate_array = []

    for _ in range(k):
        s1, s2, s3 = map(int, input().split())
        s1 -= 1
        s2 -= 1

        rotate_array.append([(s1 - s3, s2 - s3), (s1 + s3, s2 + s3)])

    visited = [False] * k
    dfs(0, grid)
    print(res)