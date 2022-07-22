import copy


def move_shark(y, x, cur, cnt, move):
    global max_eaten, shark, eaten
    if cur == 3:
        if max_eaten < cnt:
            max_eaten = cnt
            shark = [y, x]
            eaten = move[:]
        return
    for i in range(4):
        ny, nx = y+sdy[i], x+sdx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            if (ny, nx) not in set(move):
                move_shark(ny, nx, cur+1, cnt+len(tmp_grid[ny][nx]), move+[(ny, nx)])
            else:
                move_shark(ny, nx, cur+1, cnt, move)
def move_fish():
    global tmp_grid
    result = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while tmp_grid[i][j]:
                nd = tmp_grid[i][j].pop()
                for l in range(nd, nd-8, -1):
                    l %= 8
                    ny, nx = i+dy[l], j+dx[l]
                    if (ny, nx) != tuple(shark) and 0 <= ny < 4 and 0 <= nx < 4 and not smell[ny][nx]:
                        result[ny][nx].append(l)
                        break
                else:
                    result[i][j].append(nd)
    tmp_grid = copy.deepcopy(result)
def copy_complete():
    for i in range(4):
        for j in range(4):
            if tmp_grid[i][j]:
                grid[i][j] += tmp_grid[i][j]
def decrease_smell():
    for i in range(4):
        for j in range(4):
            if smell[i][j]:
                smell[i][j] -= 1


if __name__=="__main__":
    m, s = map(int, input().split())
    grid = [[[] for _ in range(4)] for _ in range(4)]
    for _ in range(m):
        fy, fx, d = map(int, input().split())
        grid[fy-1][fx-1].append(d-1)
    dy, dx = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
    sdy, sdx = [-1, 0, 1, 0], [0, -1, 0, 1]
    sy, sx = map(int, input().split())
    shark = [sy-1, sx-1]
    smell = [[0 for _ in range(4)] for _ in range(4)]
    shark_move = []
    for _ in range(s):
        eaten = []
        max_eaten = -1
        tmp_grid = copy.deepcopy(grid)
        move_fish()
        move_shark(shark[0], shark[1], 0, 0, [])
        for y, x in eaten:
            if tmp_grid[y][x]:
                tmp_grid[y][x] = []
                smell[y][x] = 3
        decrease_smell()
        copy_complete()
    answer = 0
    for i in range(4):
        for j in range(4):
            answer += len(grid[i][j])
    print(answer)
