import sys

def input():
    return sys.stdin.readline().rstrip()

def sub_ploblem(x, y, board, cnt, duple_list):
    '''
    말의 시작점 (0, 0)
    1. 말이 이동할 때 이미 지나간 알파벳은 
    지나갈 수 없음
    2. 말은 상하 좌우로 이동 가능
    3. 말이 최대한 몇칸 갈 수 있는지 확인.
    4. 말이 지나는 칸은 (0, 0)도 포함
    cnt = 1 부터 시작
    '''
    global ans
    ans = max(ans, cnt)

    for dir in dirs:
        dx, dy = x + dir[0], y + dir[1]

        if (dx < 0 or dx >= R or dy <0 or dy >= C):
            continue
        
        if not duple_list[ord(board[dx][dy]) - ord('A')]:
            duple_list[ord(board[dx][dy]) - ord('A')] = True 
            sub_ploblem(dx, dy, board, cnt + 1, duple_list)
            duple_list[ord(board[dx][dy]) - ord('A')] = False

if __name__=="__main__":
    R, C = map(int,input().split())
    board = [list(input()) for _ in range(R)]
    dirs = [(0, 1),(0, -1), (1, 0),(-1, 0)]
    ans = 0
    duple_list = [False] * 26
    duple_list[ord(board[0][0]) - ord('A')] = True
    sub_ploblem(0, 0, board, 1, duple_list)
    print(ans)