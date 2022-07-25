import sys

from itertools import combinations
import copy

def input():
    return sys.stdin.readline().rstrip()

def search_target(archers, enemy, g):
    targets = []
    for archer in archers:
        r, c = archer
        min_d = 1e9
        t_x, t_y = -1, -1
        for x, y in enemy:
            if g[x][y] == 1:
                l = abs(r - x) + abs(c - y)

                if l < min_d and l <= d:
                    min_d = l
                    t_x = x
                    t_y = y

        if t_x != -1 and t_y != -1:
            targets.append([t_x, t_y])

    return targets

def move(g, enemy):

    remove_val = []
    add_val = []
    for i in range(len(enemy)):
        r, c = enemy[i][0], enemy[i][1]

        if g[r][c] == 1:
            remove_val.append([r, c])
            if r + 1 < n:
                enemy[i][0] += 1
                add_val.append([r + 1, c])
    
    for r, c in remove_val:
        g[r][c] = 0
    
    for r, c in add_val:
        g[r][c] = 1


def remove_target(archers, g, enemy):
    _cnt = 0
    for _ in range(n):
        targets = search_target(archers, enemy, g)

        while targets:
            r, c = targets.pop()
            if g[r][c] == 1:
                _cnt += 1
                g[r][c] = 0

        move(g, enemy)
        
    
    return _cnt

if __name__ == "__main__":
    '''
        거리
        abs(r1 - r2) + abs(c1 - c2)
    '''
    n, m, d = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    case_archer = [(n, i) for i in range(m)]

    res = 0
    enemy = []
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                enemy.append([r,c])

    enemy.sort(key=lambda x: x[1])

    for archers in combinations(case_archer, 3):
        res = max(remove_target(archers, copy.deepcopy(grid), copy.deepcopy(enemy)), res)

    print(res)
