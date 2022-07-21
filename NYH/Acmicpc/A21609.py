import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution(colors):
    global score
    global grid

    while True:
        block_groups = []

        for color in colors:
            block_groups.append(block_group(color))
    
        comp = []
        max_len = 2
        for groups in block_groups:
            for group in groups:
                if group and group[-1] >= max_len:
                    max_len = group[-1]
                    comp.append(group)

        # 찾았는데 없다면?
        if not comp:
            return

        comp.sort(key=lambda x:(-x[-1], -x[-2], -x[0][0], -x[0][1]))

        # 점수 계산
        score += comp[0][-1] ** 2

        # 찾은 모든 블록을 제거
        most_group = comp[0][:-2]
        for r, c, _ in most_group:
            grid[r][c] = -2
        
        # 중력 작용
        gravity()
        # 반시계 회전
        grid = anti_clockwise(grid)
        # 중력 작용
        gravity()

    
def gravity():
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if grid[i][j] >= 1 or grid[i][j] == 0:
                r, c = i, j
                nr = r + dr[1]

                while nr < n:
                    if grid[nr][c] == -2:
                        grid[nr][c] = grid[r][c]
                        grid[r][c] = -2
                        r = nr
                        nr = r + dr[1]
                    else:
                        break

def anti_clockwise(arr):

    return list(map(list, zip(*arr)))[::-1]

def block_group(color):
    groups = []

    visited = [[False for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if grid[r][c] == color and not visited[r][c]:
                pos = (r,c)
                group = bfs(pos, color, visited)
                visited[r][c] = True
                
                if group:
                    if group[-1] >= 2:
                        groups.append(group)

    return groups

def bfs(pos, color, visited):
    
    bfs_visited = [[False for _ in range(n)] for _ in range(n)]
    bfs_visited[pos[0]][pos[1]] = True
    queue = deque([pos])
    g = []
    g.append([pos[0], pos[1], grid[pos[0]][pos[1]]])
    rainbow_cnt = 0

    while queue:
        r, c = queue.pop()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if nr < 0 or nc < 0 or nr >=n or nc >=n:
                continue
            
            # 제거된 블록
            if grid[nr][nc] == -2:
                continue

            elif (grid[nr][nc] == 0 or grid[nr][nc] == color) and not bfs_visited[nr][nc]:
                queue.appendleft([nr, nc])
                bfs_visited[nr][nc] = True
                g.append([nr, nc, grid[nr][nc]])

                if grid[nr][nc] == color:
                    visited[nr][nc] = True
                if grid[nr][nc] == 0:
                    rainbow_cnt += 1

    g.sort(key=lambda x:(-x[2], x[0], x[1]))
    g.append(rainbow_cnt)
    g.append(len(g) - 1)
    
    return g

if __name__=="__main__":
    '''
        기준블록은 무지개 블록이 아닌
        것 중에서 행 번호, 열 번호 작은 순

        1. 크기가 가장 큰 블록 그룹 찾기
        , 무지개 블록수 많은 블록 그룹 찾기
        , 기준 블록 행이 가장 큰 것
        , 열이 가장 큰 것

        2. 1에서 찾은 블록 그룹의 모든 블록을 제거
        점수는 총 블록 수가 B라고 할 때 B^2 점 획득 
        3. 격자에 중력 작용
        4. 격자가 90도 반시계 방향 회전
        5. 다시 격자에 중력 작용

        중력 작용 시 검은색 블록을 제외한 모든 블록이 
        행의 번호가 큰 칸으로 이동.
        다른 블록이나 격자의 경계를 만나기 전가지 계속
    '''
    n, m = map(int, input().split())
    colors = [i for i in range(1, m + 1)]
    grid = [list(map(int, input().split())) for _ in range(n)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    score = 0
    solution(colors)
    print(score)
