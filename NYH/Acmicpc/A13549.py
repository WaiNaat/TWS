import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

def solution():
    N, K = map(int, input().split())

    heap = []
    INF = 100001
    heapq.heappush(heap, (0, N))
    dp = [INF] * INF
    dp[N] = 0

    while heap:
        time , cur = heapq.heappop(heap)

        if cur == K:
            return time
        
        if cur + 1 < INF and time < dp[cur + 1]:
            dp[cur + 1] = min(dp[cur] + 1, dp[cur + 1])
            heapq.heappush(heap, (time + 1, cur + 1))
        
        if cur * 2 < INF and time < dp[cur * 2]:
            dp[cur * 2] = dp[cur]
            heapq.heappush(heap, (time, cur * 2))
        
        if cur - 1 >= 0 and time < dp[cur - 1]:
            dp[cur - 1] = dp[cur] + 1
            heapq.heappush(heap, (time + 1, cur - 1))
    
if __name__ == "__main__":
    print(solution())
    
