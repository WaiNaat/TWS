import sys
from itertools import permutations
def input():
    return sys.stdin.readline().rstrip()


def solution(N, board, sign_cnt):

    # 준비 작업
    sign = ['+', '-', '*', '/']
    signs = []
    idx = 0
    for cnt in sign_cnt:
        for x in range(cnt):
            signs.append(sign[idx])
        idx+= 1

    min_num = 1e9
    max_num = -1e9

    for permu in permutations(signs, N - 1):
        num = board[0]
        for x in range(1, N):
            if permu[x - 1] == '+':
                num += board[x]
            elif permu[x - 1] == '-':
                num -= board[x]
            elif permu[x - 1] == '*':
                num *= board[x]
            else:
                if num < 0:
                    num = -(abs(num) // abs(board[x]))
                else:
                    num //= board[x]
        min_num = min(min_num, num)
        max_num = max(max_num, num)

    return [max_num, min_num]

if __name__=="__main__":
    
    N = int(input())
    board = list(map(int,input().split()))
    sign_cnt = list(map(int,input().split()))
    for sol in solution(N, board, sign_cnt):
        print(sol)