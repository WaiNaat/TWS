import sys
from collections import deque
'''

백준이 태울 승객을 고를 때는 현재 위치에서 최단거리가 가장 짧은 승객을 고른다. 
그런 승객이 여러 명이면 그중 행 번호가 가장 작은 승객을, 
그런 승객도 여러 명이면 그중 열 번호가 가장 작은 승객을 고른다.
태워 이동하면서 소모한 연료 양의 두 배가 충전된다.
승객을 목적지로 이동시킨 동시에 
연료가 바닥나는 경우는 실패한 것으로 간주하지 않는다.
단, 이동 도중에 연료가 바닥나서 
다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다.
모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.
'''
def input():
    return sys.stdin.readline().rstrip()

def move(g):
    global taxi
    visited = [[False for _ in range(n)] for _ in range(n)]

    g_taxi = deque([taxi])
    r, c = taxi
    g[r][c] = 0
    visited[r][c] = True

    while g_taxi:
        r, c = g_taxi.pop()
        for dir in dirs:
            nr = r + dir[0]
            nc = c + dir[1]

            if nr < 0 or nr >=n or nc < 0 or nc >= n:
                continue
            
            if g[nr][nc] == -1 or visited[nr][nc] :
                continue

            g[nr][nc] = g[r][c] + 1
            visited[nr][nc] = True
            g_taxi.appendleft((nr, nc))

    return g

if __name__ =="__main__":
    
    n, m, gas = map(int ,input().split())
    grid = []
    for _ in range(n):
        data = list(map(int,input().split()))
        array = []
        for d in data:
            if d == 1:
                array.append(-1)
            else:
                array.append(-2)
        grid.append(array)


    # 택시 출발 행 열
    t_r, t_c = map(int,input().split())
    guests = []

    for _ in range(m):
        x1, y1, x2, y2 = map(int,input().split())
        guests.append([x1 - 1, y1 - 1, x2 - 1, y2 - 1])

    # 방향
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    taxi = [t_r - 1, t_c - 1] 

    while True:

        if not guests:
            break

        g = [item[:] for item in grid]
        start_grid = move(g)

        sort_guest = []

        for guest in guests:
            sr, sc, dr, dc = guest
            cost = start_grid[sr][sc]

            if cost < 0:
                continue

            sort_guest.append([cost, sr, sc, dr, dc])

        if not sort_guest:
            print(-1)
            exit()
        else:
            sort_guest.sort(key=lambda x:(x[0], x[1], x[2]))

            cost, sr, sc, dr, dc = sort_guest.pop(0)

            target = [sr, sc, dr, dc]

            # 소모량이 보유량보다 많으면
            if cost > gas:
                print(-1)
                exit()
            else:
                gas -= cost
                taxi = [sr, sc]

                g = [item[:] for item in grid]
                end_grid = move(g)
                
                # 목적지 도달
                cost = end_grid[dr][dc]

                # 갈 수 없는 곳이면?
                if cost < 0:
                    print(-1)
                    exit()
                
                gas -= cost

                if gas >= 0:
                    gas += cost * 2
                    guests.remove(target)
                    taxi = [dr, dc]
                else:
                    print(-1)
                    exit()

    print(gas)
    
    