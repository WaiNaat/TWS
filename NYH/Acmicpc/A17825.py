import sys

'''
파란색 화살표
말들의 위치를 어떻게 표현할 것인가?
'''
def input():
    return sys.stdin.readline().rstrip()


def length_check(r, c):
    # 길이를 넘으면?
    if len(board[c]) <= r:
        return False
    else:
        return True

def dfs(depth, score):
    global max_score
    if depth == 10:
        max_score = max(score, max_score)
        return


    for i in range(len(horse)):
        
        r, c = horse[i]

        # 길이를 넘지 않으면서
        if length_check(r, c):
            nr = r + dice[depth]
            nc = c
            
            if c == 0:

                # 길이를 넘지 않으면서
                if length_check(nr, nc):
                    if nr == 5:
                        nr, nc = 0, 1
                    if nr == 10:
                        nr, nc = 1, 2
                    if nr == 15:
                        nr, nc = 0, 3


            if length_check(nr,nc):
                if board[nc][-1] == board[nc][nr]:
                    nc = 0
                    nr = 20

                elif nc >= 1 and nr >= 4:
                    nc = 1
            
            if [nr, nc] not in horse or not length_check(nr, nc): 
                horse[i] = [nr, nc]
                try:
                    calc = score + board[nc][nr]
                except:
                    calc = score
                dfs(depth + 1, calc)
                horse[i] = [r, c]
    return



if __name__=="__main__":
    dice = list(map(int,input().split()))
    board = [
        [i * 2  for i in range(21)],
        [10, 13, 16, 19, 25, 30, 35, 40],
        [-1, 20, 22, 24, 25, 30, 35, 40],
        [30, 28, 27, 26, 25, 30, 35, 40]
    ]

    # 좌표, special 포함 여부(0 이면 미포함,) 
    horse = [[0, 0], [0, 0], [0, 0], [0, 0]]
    max_score = 0
    dfs(0, 0)
    print(max_score)
