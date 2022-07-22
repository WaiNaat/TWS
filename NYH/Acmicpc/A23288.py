import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def rotate(d):

    if d == 0:
        # 동쪽 이동
        # 위, 오른쪽, 아래, 왼쪽 순
        # => 왼쪽, 위, 오른쪽, 아래 순
        dice[1], dice[6], dice[2], dice[5] = dice[5], dice[1], dice[6], dice[2]
        
    elif d == 1:
        # 서쪽 이동
        # 위, 오른쪽, 아래, 왼쪽 순
        # => 오른쪽, 아래, 왼쪽, 위 순
        dice[1], dice[6], dice[2], dice[5] = dice[6], dice[2], dice[5], dice[1]
    elif d == 2:
        # 남쪽 이동
        # 위, 앞, 아래, 뒤 순
        # 뒤, 위, 앞, 아래 순
        dice[1], dice[3], dice[2], dice[4] = dice[4], dice[1], dice[3], dice[2]
    elif d == 3:
        # 북쪽 이동
        # 위, 앞, 아래, 뒤 순
        # 앞, 아래, 뒤, 위 순
        dice[1], dice[3], dice[2], dice[4] = dice[3], dice[2], dice[4], dice[1]


def bfs(r, c, score):

    q = deque([[r, c]])

    _cnt = 1

    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[r][c] = True

    while q:
        r, c = q.pop()
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            
            if grid[nr][nc] == score and not visited[nr][nc]:
                q.appendleft((nr, nc))
                visited[nr][nc] = True
                _cnt += 1


    return score * _cnt


if __name__=="__main__":
    '''
      2
    4 1 3
      5
      6

    위 idx 1 1
    아래 idx 2 6
    앞 idx 3 5
    뒤 idx 4 2
    왼쪽 idx 5 4
    오른쪽 idx 6 3
    '''
    dice = [0, 1, 6, 5, 2, 4, 3]

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    # 초기 방향 동쪽
    d = 0

    n, m, k = map(int, input().split())

    grid = [list(map(int,input().split())) for _ in range(n)]

    r, c = 0, 0
    sum_score = 0
    for _ in range(k):

        nr = r + dr[d]
        nc = c + dc[d]

        # 이동 방향에 칸이 없다면?
        if nr < 0 or nr >= n or nc < 0 or nc >= m:

            if d == 0: d = 1
            elif d == 1: d = 0
            elif d == 2: d = 3
            elif d == 3: d = 2

            nr = r + dr[d]
            nc = c + dc[d]
        
        rotate(d)

        score = grid[nr][nc]
        scores = bfs(nr, nc, score)
        under = dice[2]
        sum_score += scores

        # A > B
        if under > score:
            if d == 3: d = 0
            elif d == 0: d = 2
            elif d == 2: d = 1
            elif d == 1: d = 3

        # A < B
        elif under < score:
            if d == 3: d = 1
            elif d == 2: d = 0
            elif d == 1: d = 2
            elif d == 0: d = 3

        r, c = nr, nc
        
    
    print(sum_score)

