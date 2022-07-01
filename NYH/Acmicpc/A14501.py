import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(calendar):
    dp = [0] * (N + 2)

    # times는 각 일자마다 값을 가지고 있다. 1일 => 1일(2일) 2일 => 2일(4일)
    # i + times[i] 가 상담이 종료되는 시간이다. 1 + 1 => 2일

    times = [0]
    prices = [0]

    for time, price in calendar:
        times.append(time)
        prices.append(price)

    for i in range(2, N + 2):       
        for j in range(1, i):
            # j + times[j] <= 2 이면? 
            # dp [i] = max(dp[j] + prices[j] or dp[i - 1] or dp[i])
            if j + times[j] <= i:
                dp[i] = max(dp[i], dp[i - 1], prices[j] + dp[j])
        
    return dp[N + 1]

if __name__=="__main__":
    N = int(input())
    calendar = [list(map(int,input().split())) for _ in range(N)]
    print(solution(calendar))