import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    
    dp[0][0][1] = 1
    # 1행 처리
    for i in range(2, n):
        if grid[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]
    
    for r in range(1, n):
        for c in range(1, n):
            
            # 대각선
            if grid[r][c] == 0 and grid[r - 1][c] == 0 and grid[r][c - 1] == 0:
                dp[2][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
            
            # 가로 세로
            if grid[r][c] == 0:
                # 가로
                dp[0][r][c] = dp[0][r][c - 1] + dp[2][r][c - 1]
                # 세로
                dp[1][r][c] = dp[1][r - 1][c] + dp[2][r - 1][c]

    _sum = 0
    for i in range(3):
        _sum += dp[i][n - 1][n - 1]
    print(_sum)
    

if __name__ =="__main__":
    n = int(input())
    res = 0
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
    solve()