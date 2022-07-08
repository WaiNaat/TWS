import sys
import heapq
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solution(shark):

    cnt = 0 
    while True:
        t, r, c, success = sub_ploblem(shark)

        if not success:
            break

        board[r][c] = 0
        cnt += t

        shark[0], shark[1] = r, c

        if shark[3] == 1:
            shark[3] = shark[2] + 1
            shark[2] += 1
        else:
            shark[3] -= 1

        
    
    return cnt
        
def sub_ploblem(shark):

    R , dirs = len(board), [(-1, 0 ), (0, -1), (1, 0), (0, 1)]

    shark_r, shark_c, shark_w, shark_req = shark
    
    search = deque([[shark_r, shark_c, 0]])
    
    fish = []
    visited = [[False for _ in range(R)] for _ in range(R)]

    while search:
        r, c, t = search.pop()

        if visited[r][c]:
            continue
        
        visited[r][c] = True

        if 0 < board[r][c] and board[r][c] < shark_w:
            # dist, row, col
            heapq.heappush(fish, (t, r, c, True))


        for dir in dirs:
            nr, nc = r + dir[0], c + dir[1]

            # 범위 초과
            if nr < 0 or nr >= R or nc < 0 or nc >= R:
                continue
            
            # 크기가 커서 지나갈 수 없음.
            if board[nr][nc] > shark_w:
                continue
            
            search.appendleft((nr, nc, t + 1))

    
    if not fish:
        return (0, 0, 0, False)

    # 가장 시간이 적게 걸린(거리가 짧은), 가장 윗행, 왼쪽열 을 반환
    return heapq.heappop(fish)



if __name__=="__main__":

    n = int(input())
    board = [list(map(int, input().split()))for _ in range(n)]

    for row in range(n):
        for col in range(n):
            if board[row][col] == 9:
                # x, y, 크기, 남은 물고기
                shark = [row, col, 2, 2]
                board[row][col] = 0
            
    

    print(solution(shark))
