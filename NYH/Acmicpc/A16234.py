import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def sub_problem(visited):

    sub_visited = [item[:] for item in visited]

    unions = []
    for i in range(n):
        for j in range(n):
            if not sub_visited[i][j]:
                union = deque([[i, j]])
                union_member = []
                sum_score = 0
                while union:
                    r, c = union.pop()
                    if sub_visited[r][c]:
                        continue

                    cur_score = board[r][c]
                    sum_score += cur_score
                    union_member.append((r, c))
                    sub_visited[r][c] = True
                                       

                    for d in range(4):
                        dr, dc = r + dirs[d][0], c + dirs[d][1]

                        if dr < 0 or dr >= n or dc < 0 or dc >= n:
                            continue

                        if sub_visited[dr][dc]:
                            continue

                        if abs(board[dr][dc] - cur_score) >= L and abs(board[dr][dc] - cur_score) <= R:
                            union.appendleft([dr, dc])

                if len(union_member) > 1:
                    union_member.append(sum_score)
                    unions.append(union_member)
    if unions:
        for member in unions:
            avg_score = member[-1] // (len(member) - 1)
            for i in range(len(member) - 1):
                row, col = member[i]
                board[row][col] = avg_score
        return True
    else:
        return False

if __name__=="__main__":
    n, L, R = map(int,input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        population = list(map(int, input().split()))
        for j in range(n):
            board[i][j] = population[j]

    dirs = [(0, 1),(1, 0), (0, -1), (-1, 0)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    while sub_problem(visited):
        cnt +=1 
    print(cnt)
    