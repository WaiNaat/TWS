import sys

def input():
    return sys.stdin.readline().rstrip()

def ladder_game():
    for i in range(1, n + 1):
        c = i
        for j in range(1, h + 1):
            c = board[j][c]
        if c != i:
            return False
    return True


def sub_ploblem(depth, idx, x, y):
    if depth == idx:
        if ladder_game():
            print(idx)
            exit()
        return
    
    for i in range(1, h + 1):
        for j in range(1, n):
            if board[i][j] == j and board[i][j + 1] == j + 1 and (i >= x or j <= y):
                board[i][j] = j + 1
                board[i][j + 1] = j
                sub_ploblem(depth + 1, idx, i, j)
                board[i][j] = j
                board[i][j + 1] = j + 1


if __name__=="__main__":

    n, m, h = map(int, input().split())
    board = [[i for i in range(n + 1)] for _ in range(h + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        board[a][b] = b + 1
        board[a][b + 1] = b
    
    for i in range(0, 4):
        sub_ploblem(0, i, 0, 0)

    print(-1)



