import sys

def input():
    return sys.stdin.readline().rstrip()

def solution():
    '''
    (0, 0) 으로 테트로미노를 만들어보자
    '''
    table = [

        [[0, 0], [0, 1], [1, 0], [1, 1]],

        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [1, 0], [2, 0], [3, 0]],

        [[0, 0], [1, 0], [2, 0], [2, 1]],
        [[0, 0], [1, 0], [0, 1], [0, 2]],
        [[0, 0], [0, 1], [1, 1], [2, 1]],
        [[0, 0], [0, 1], [0, 2], [-1, 2]],
        [[0, 0], [0, 1], [1, 0], [2, 0]],
        [[0, 0], [0, 1], [0, 2], [1, 2]],
        [[0, 0], [1, 0], [2, 0], [2, -1]],
        [[0, 0], [-1, 0], [0, 1], [0, 2]],
        
        [[0, 0], [1, 0], [1, 1], [2, 1]],
        [[0, 0], [-1, 1], [0, 1], [-1, 2]],
        [[0, 0], [0, 1], [1, 1], [1, 2]],
        [[0, 0], [1, 0], [1, -1], [2, -1]],
    
        [[0, 0], [1, -1], [1, 0], [1, 1]],
        [[0, 0], [1, 0], [1, 1], [2, 0]],
        [[0, 0], [0, 1], [0, 2], [1, 1]],
        [[0, 0], [1, 0], [1, -1], [2, 0]]
    ]

    max_sum = 0
    for row in range(N):
        for col in range(M):
            for dirs in table:
                is_check = True
                cur_sum = 0
                for i in range(4):
                    dx, dy = row + dirs[i][0], col + dirs[i][1]
                    if dx < 0 or dx >= N or dy < 0 or dy >= M:
                        is_check = False
                        break
                    cur_sum += paper[dx][dy]

                if is_check:
                    max_sum = max(max_sum, cur_sum)

    return max_sum



if __name__=="__main__":
    N, M = map(int,input().split())
    paper = [list(map(int,input().split())) for _ in range(N)]
    print(solution())
    