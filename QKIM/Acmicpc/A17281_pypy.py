import sys
from itertools import permutations
input = sys.stdin.readline

# functions
def play_game(batters):
    score = 0
    batter_idx = 0

    for inning in range(N):
        out = 0
        base1 = base2 = base3 = False
        inning_info = info[inning]

        while out < 3:
            batter_result = inning_info[batters[batter_idx]]

            if batter_result == 0:
                out += 1

            elif batter_result == 1:
                if base3: score += 1
                base1, base2, base3 = True, base1, base2

            elif batter_result == 2:
                if base3: score += 1
                if base2: score += 1
                base1, base2, base3 = False, True, base1
            
            elif batter_result == 3:
                if base3: score += 1
                if base2: score += 1
                if base1: score += 1
                base1, base2, base3 = False, False, True
            
            else:
                if base3: score += 1
                if base2: score += 1
                if base1: score += 1
                score += 1
                base1 = base2 = base3 = False                

            batter_idx = (batter_idx + 1) % 9

    return score

# input
N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]

# process
sol = 0

for p in permutations(range(1, 9)):
    p = list(p)
    batters = p[:3] + [0] + p[3:]
    sol = max(play_game(batters), sol)

# output
print(sol)