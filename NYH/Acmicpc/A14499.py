import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(dice, dice_direction):

    x, y = dice
    bottom_pos, top_pos = 6, 1

    for dice_dir in dice_direction:
        dx = x + dirs[dice_dir][0]
        dy = y + dirs[dice_dir][1]

        # 보드를 넘어가면 명령 무시
        if dx < 0 or dx >= n or dy < 0 or dy >= m:
            continue
        
        # 주사위를 움직인다.
        move_dice(dice_dir)

        if board[dx][dy] == 0:
            # 지도의 값이 0 이라면?
            board[dx][dy] = dice_val[bottom_pos]
        else:
            # 지도의 값이 0이 아니라면
            dice_val[bottom_pos] = board[dx][dy]
            board[dx][dy] = 0
        
        x = dx
        y = dy
        print(dice_val[top_pos])


def move_dice(dice_dir):
    
    if dice_dir == 1:
        dice_val[1], dice_val[3], dice_val[4], dice_val[6] = dice_val[4], dice_val[1], dice_val[6], dice_val[3]
    if dice_dir == 2:
        dice_val[1], dice_val[3], dice_val[4], dice_val[6] = dice_val[3], dice_val[6], dice_val[1], dice_val[4]
    if dice_dir == 3:
        dice_val[1], dice_val[2], dice_val[5], dice_val[6] = dice_val[5], dice_val[1], dice_val[6], dice_val[2]
    if dice_dir == 4:
        dice_val[1], dice_val[2], dice_val[5], dice_val[6] = dice_val[2], dice_val[6], dice_val[1], dice_val[5]    
                



if __name__=="__main__":
    '''
        1 동쪽, 2 서쪽, 3 북쪽, 4 남쪽
    '''
    n, m, x, y, k = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dice_direction = list(map(int,input().split()))
    dirs = [(),(0, 1), (0, -1), (-1, 0), (1, 0)]
    dice = [x, y]
    dice_val = [0] * 7
    solution(dice, dice_direction)