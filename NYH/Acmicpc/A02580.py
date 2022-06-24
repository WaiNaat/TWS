import sys

def input():
    return sys.stdin.readline().rstrip()

def possible_numbers(row, col, board):
    # 1번 조건 가로
    possible = set(numbers) - set(board[row])

    # 1번 조건 세로
    possible = list(possible - set([x[col] for x in board]))

    return possible

def sub_ploblem(idx):
    '''
        1. 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가
        한번씩만 나타난다. possible_numbers
        2. 굵은 선으로 구분되어 있는 3*3 숫자 안에서도 
        1부터 9까지의 숫자가 한번씩 나타나야한다.

        row 0 ~ 2 and col 0 ~2
    '''
    if idx == check_zero:
        for i in range(9):
            print(' '.join(map(str, board[i])))
        exit(0)

    x, y = zero_place[idx] // 9, zero_place[idx] % 9
    square = check_square(x, y)
    possible_list = possible_numbers(x, y, board)
    for possible in possible_list:
        if not board_check[square][possible]:
            board[x][y] = possible
            board_check[square][possible] = True
            sub_ploblem(idx + 1)
            board[x][y] = 0
            board_check[square][possible] = False



def check_square(row, col):
    # 몇 사분면인지 확인
    return row // 3 * 3 + col //3

if __name__=="__main__":
    board = [list(map(int,input().split())) for _ in range(9)]
    numbers = [i for i in range(1, 10)] 
    board_check = [[False] * 10 for _ in range(9)]
    check_zero = 0
    zero_place = [0] * 81
    for row in range(9):
        for col in range(9):
            number = board[row][col]
            if board[row][col]:
                board_check[check_square(row, col)][number] = True
            else:
                zero_place[check_zero] = row * 9 + col
                check_zero += 1
    sub_ploblem(0)
