import sys

def green_calc(t, r, c):
    global score
    if t == 1:
        # 테트리스 이동
        while r < 6:
            if green[r][c] != 1:
                r += 1
            else:
                break

        r -= 1
        green[r][c] = 1

        for i in range(2, 6):
            # 한 행이 가득 찼다면?
            if sum(green[i]) == 4:
                score += 1
                green[0 + 1 : i + 1] = green[:i]
                green[0] = [0 for _ in range(4)]

        # 연한 구역에 멈췄다면? 
        if r == 1 and green[r][c] == 1:
            # 행 이동
            green[2:] = green[1:5]
            green[1] = [0 for _ in range(4)]
            
    elif t == 2:
        while r < 6:
            if green[r][c] != 1 and green[r][c + 1] != 1:
                r += 1
            else:
                break

        r -= 1
        green[r][c] = 1
        green[r][c + 1] = 1  

        for i in range(2, 6):
            # 한 행이 가득 찼다면?
            if sum(green[i]) == 4:
                score += 1
                green[0 + 1 : i + 1] = green[:i]
                green[0] = [0 for _ in range(4)]

        if r == 1 and green[r][c] == 1:
            # 행 이동
            green[2:] = green[1:5]
            green[1] = [0 for _ in range(4)]
            
        
    elif t == 3:
        while r < 6:
            if green[r][c] != 1:
                r += 1
            else:
                break
        r -= 1
        green[r - 1][c] = 1
        green[r][c] = 1
        for i in range(2, 6):
            # 한 행이 가득 찼다면?
            if sum(green[i]) == 4:
                score += 1
                green[0 + 1 : i + 1] = green[:i]
                green[0] = [0 for _ in range(4)]

        # 끝 칸에 곂친 경우
        if r == 1 and green[r - 1][c] == 1 and green[r][c] == 1:
            green[2:] = green[0: 4]
            green[0] = [0 for _ in range(4)]
            green[1] = [0 for _ in range(4)]

        # 앞칸만 곂친 경우
        elif r == 1 and green[r][c] == 1:
            green[2:] = green[1:5]
            green[1] = [0 for _ in range(4)]

        # 앞칸만 곂친 경우
        elif r == 2 and green[r - 1][c] == 1:
            green[2:] = green[1:5]
            green[1] = [0 for _ in range(4)]
            

def blue_calc(t, r, c):
    global score
    if t == 1:
        # 이동
        while c < 6:
            if blue[r][c] != 1:
                c += 1
            else:
                break

        c -= 1
        blue[r][c] = 1

        # 점수 계산
        _sum = 0
        for i in range(4):
            _sum += blue[i][c]

        if _sum == 4:
            score += 1
            for i in range(4):
                blue[i][1: c + 1] = blue[i][:c]
        # 연한 구역에서 멈춘다면
        if c == 1 and blue[r][c] == 1:
            for i in range(4):
                blue[i][2:] = blue[i][1: 5]
            
            blue[r][c] = 0
        
            
    if t == 2:
        while c < 6:
            if blue[r][c] != 1:
                c += 1
            else:
                break

        c -= 1
        blue[r][c - 1] = 1
        blue[r][c] = 1

        # 점수 계산
        _sum = 0
        for i in range(4):
            _sum += blue[i][c - 1]

        if _sum == 4:
            score += 1
            for i in range(4):
                blue[i][1: c] = blue[i][:c - 1]

        _sum = 0
        for i in range(4):
            _sum += blue[i][c]

        if _sum == 4:
            score += 1
            for i in range(4):
                blue[i][1: c + 1] = blue[i][:c]

        # 끝 칸에 곂친 경우
        if c == 1 and blue[r][c - 1] == 1 and blue[r][c] == 1:
            # 칸을 두칸 땡긴다
            for i in range(4):
                blue[i][2:] = blue[i][0: 4]

            blue[r][c - 1] = 0
            blue[r][c] = 0

        # 한칸 겹친 경우
        elif c == 1 and blue[r][c] == 1:
            for i in range(4):
                blue[i][2:] = blue[i][1: 5]
            blue[r][c - 1] = 0 
                
        # 한 칸 곂친 경우
        elif c == 2 and blue[r][c - 1] == 1:
            for i in range(4):
                blue[i][2:] = blue[i][1: 5]
            
            blue[r][c - 1] = 0 

    if t == 3:
        while c < 6:
            if blue[r][c] != 1 and blue[r + 1][c] != 1:
                c += 1
            else:
                break

        c -= 1
        blue[r][c] = 1
        blue[r + 1][c] = 1

        # 점수 계산
        _sum = 0
        for i in range(4):
            _sum += blue[i][c]
    
        if _sum == 4:
            score += 1
            for i in range(4):
                blue[i][1: c + 1] = blue[i][:c]

        if c == 1 and blue[r][c] == 1:
            for i in range(4):
                blue[i][2:] = blue[i][1: 5]
            
            blue[r][c] = 0
            blue[r + 1][c] = 0
            

def input():
    return sys.stdin.readline().rstrip()

if __name__=="__main__":
    n = int(input())
    
    red = [[0 for _ in range(4)] for _ in range(4)]
    green = [[0 for _ in range(4)] for _ in range(6)]
    blue = [[0 for _ in range(6)] for _ in range(4)]
    score = 0

    for _ in range(n):
        t, x, y = map(int, input().split())

        green_calc(t, 0, y)
        blue_calc(t, x, 0)
    
    cnt = 0
    for c in range(4):
        for r in range(2, 6):
            if green[r][c] == 1:
                cnt += 1
            if blue[c][r] == 1:
                cnt += 1
            
    res = [str(score), str(cnt)]
    print("\n".join(res))
    
