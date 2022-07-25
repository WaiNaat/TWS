import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()


def baseball(order):
    
    score = 0
    idx = -1
    '''
        안타를 치면 
        해당 타석 
        ground True
        이동된 곳 ground False

        문제가 좀 시간복잡도 빡빡.
    '''
    for i in range(n):
        _out = 0
        g1, g2, g3 = 0, 0, 0

        while _out < 3:
            idx = (idx + 1) % 9

            # 아웃인 경우
            if hits[i][order[idx]] == 0:
                _out += 1
            
            # 안타
            elif hits[i][order[idx]] == 1:
                score += g3
                g1, g2, g3 = 1, g1, g2

            # 2루타
            elif hits[i][order[idx]] == 2:
                score += g3 + g2
                g1, g2, g3 = 0, 1, g1
            
            # 3루타
            elif hits[i][order[idx]] == 3:

                score += g3 + g2 + g1
                g1, g2, g3 = 0, 0, 1

            # 홈런
            elif hits[i][order[idx]] == 4:
                
                score += g3 + g2 + g1 + 1
                g1, g2, g3 = 0, 0, 0

    return score


if __name__=="__main__":
    n = int(input())
    hits = []

    for _ in range(n):
        l = list(map(int, input().split()))
        hits.append(l)

    res = 0

    case = [i for i in range(1, 9)]
    
    for permu in permutations(case, 8):
        p = list(permu)
        p.insert(3, 0)
        score = baseball(p)
        if res < score:
            res = score

    print(res)