import sys 
def input():
    return sys.stdin.readline().rstrip()

def create_curve(curve_info):
    c, r, d, g = curve_info

    curve_d = [d]
    board[r][c] = 1
    for _ in range(1, g + 1):
        curve = []
        for j in range(len(curve_d) - 1, -1 , -1):
            curve.append((curve_d[j] + 1) % 4)
        curve_d.extend(curve)

    for d in curve_d:
        r, c = r + dirs[d][0], c + dirs[d][1]
        board[r][c] = 1



if __name__=="__main__":
    N = int(input())
    dragon_curve = [list(map(int, input().split())) for _ in range(N)]
    dirs = [(0, 1), (-1, 0), (0, -1),(1, 0)]
    board = [[0 for _ in range(101)] for _ in range(101)]

    for curve in dragon_curve:
        create_curve(curve)

    cnt = 0
    for i in range(100):
        for j in range(100):
            if board[i][j] and board[i][j + 1] and board[i + 1][j] and board[i + 1][j + 1]:
                cnt += 1
    print(cnt)