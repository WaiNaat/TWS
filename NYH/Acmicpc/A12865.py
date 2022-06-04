import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    n, k = map(int, input().split())
    backpack = [list(map(int,input().split())) for _ in range(n)]
    dp = [0 for _ in range(k + 1)]

    for back in backpack:
        w, v = back
        for i in range(k, 0, -1):
            if i >= w:
                dp[i] = max(dp[i], dp[i - w] + v)
        
    print(dp[k])

solution()
