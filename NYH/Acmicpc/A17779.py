import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    global res
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            for d1 in range(1, n + 1):
                for d2 in range(1, n + 1):
                    if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y < y + d2 <= n:
                        res = min(res, sub_ploblem(x, y, d1, d2))


def sub_ploblem(x, y, d1, d2):
    g = [[0]*(n+1) for _ in range(n+1)]
    people = [0, 0, 0, 0, 0]
    

    g[x][y] = 5
    for i in range(1, d1+1):
        g[x+i][y-i] = 5
    for i in range(1, d2+1):
        g[x+i][y+i] = 5
    for i in range(1, d2+1):
        g[x+d1+i][y-d1+i] = 5
    for i in range(1, d1+1):
        g[x+d2+i][y+d2-i] = 5


    # 1
    for i in range(1, x+d1):
        for j in range(1, y+1):
            if g[i][j] == 5:
                break
            else:
                people[0] += graph[i][j]

    # 2
    for i in range(1, x+d2+1):
        for j in range(n, y, -1):
            if g[i][j] == 5:
                break
            else:
                people[1] += graph[i][j]

    # 3
    for i in range(x+d1, n+1):
        for j in range(1, y-d1+d2):
            if g[i][j] == 5:
                break
            else:
                people[2] += graph[i][j]
    # 4
    for i in range(x+d2+1, n+1):
        for j in range(n, y-d1+d2-1, -1):
            if g[i][j] == 5:
                break
            else:
                people[3] += graph[i][j]

    people[4] = total - sum(people[0:4])
    return max(people) - min(people)

if __name__=="__main__":
    n = int(input())
    graph = [[0 for _ in range(n + 1)]] + [[0] + list(map(int, input().split())) for _ in range(n)]

    total = 0
    for g in graph:
        total += sum(g)
    res = 1e9
    solution()
    print(res)