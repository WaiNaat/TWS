import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(robot):
    '''
    BOARD
    0 : 빈칸
    1 : 벽

    dirs
    왼쪽 회전 (현재 위치 + 3) % 4

    청소하고 해당 칸을 2로 변경
    '''
    is_check = True
    cnt = 0
    while is_check:
        x, y, robot_dir = robot
        left_check = False

        if board[x][y] == 0:
            cnt += 1
            board[x][y] = 2

        left_rotate = robot_dir

        for _ in range(4):
            left_rotate = (left_rotate + 3) % 4
            dx, dy = x + dirs[left_rotate][0], y + dirs[left_rotate][1]
            if board[dx][dy] == 0:
                # 칸이 청소되지 않았으면 이동
                robot_dir = left_rotate
                robot = (dx, dy, robot_dir)
                left_check = True
                break

        if left_check:
            # 왼칸이 비어서 이동했으면 뒤의 동작을 생략
            continue
        
        else:
            # 왼칸 4번 회전시에도 빈칸을 못찾았다면? 3 -> 1 1 -> 3 2 -> 0 0-> 2
            dx, dy = x + dirs[(left_rotate + 2) % 4][0], y + dirs[(left_rotate + 2) % 4][1]
            if board[dx][dy] == 1:
                is_check = False
            else:
                robot = (dx, dy, robot_dir)
    

    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())
    R, C, D = map(int, input().split())

    board = [list(map(int,input().split())) for _ in range(N)]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    robot = (R, C, D)
    print(solution(robot))