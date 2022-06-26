import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()


def solution(board, snake_direction):

    snake_queue = deque()
    snake_direction = deque(snake_direction)
    snake_queue.append([0, 0])
    dir_num = 0
    cur_dir = dirs[dir_num]
    cur_sec = 0
    
    while snake_queue:
        x, y = snake_queue.pop()
        
        if snake_direction and cur_sec == int(snake_direction[0][0]):
            snake_sec, snake_dir = snake_direction.popleft()
            if snake_dir == "L":
                dir_num = (dir_num + 3) % 4
            elif snake_dir == "D":
                dir_num = (dir_num + 1) % 4
        
        cur_dir = dirs[dir_num]
        
        dx = x + cur_dir[0]
        dy = y + cur_dir[1]

        # 벽에 부딪힘
        if dx < 0 or dx >= N or dy < 0 or dy >= N:
            return cur_sec + 1
        
        # 몸에 부딪힘
        if (dx, dy) in snake_queue:
            return cur_sec + 1
        
        if board[dx][dy] == 1:
            snake_queue.append((x, y))
            board[dx][dy] = 0
        elif board[dx][dy] == 0:
            # 사과가 없을 때 꼬리를 머리부분으로 땡긴다.
        
            if len(snake_queue) == 1:
                snake_queue.pop()
                snake_queue.append((x,y))
            elif len(snake_queue) >= 2:
                snake_queue = deque(list(snake_queue)[1:])
                snake_queue.append((x, y))
        snake_queue.append((dx, dy))

        cur_sec += 1

if __name__=="__main__":
    N = int(input())
    K = int(input())
    apples = [list(map(int, input().split())) for _ in range(K)]
    L = int(input())
    snake_direction = []
    for _ in range(L):
        snake_sec, snake_dir = input().split()
        snake_direction.append([snake_sec, snake_dir])
    board = [[0 for _ in range(N)] for _ in range(N)]
    for apple in apples:
        x, y = apple
        board[x - 1][y - 1] = 1
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    print(solution(board, snake_direction))