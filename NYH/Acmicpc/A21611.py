import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def magic(order):
    d, s = order

    r, c = s_r, s_c

    while 0 <= r < n and 0 <= c < n and s != 0:
        r = r + dr[d]
        c = c + dc[d]

        # 삭제
        grid[r][c] = 0
        s -= 1

    # 빈 공간 없이 이동
    move(get_marbles())
    bomb = [0, 0, 0]
    while duplicate_check():
        _one, _two, _three = explosion()
        bomb[0] += _one
        bomb[1] += _two
        bomb[2] += _three

    marbles = get_marbles()
    if marbles:
        group_marbles = deque()

        p_v = marbles.popleft()
        _cnt = 1

        while marbles:
            v = marbles.popleft()

            if p_v == v:
                _cnt += 1
            else:
                group_marbles.append(_cnt)
                group_marbles.append(p_v)
                p_v = v
                _cnt = 1

        group_marbles.append(_cnt)
        group_marbles.append(p_v)

        if len(group_marbles) > n * n:
            group_marbles = list(group_marbles)[:n * n]
            group_marbles = deque(group_marbles)

        move(group_marbles)
    return bomb

def duplicate_check():
    marbles = get_marbles()

    if not marbles or len(marbles) < 4:
        return False

    elif marbles:
        p_v = marbles.popleft()

        _cnt = 1
        while marbles:
            v = marbles.popleft()
            if p_v == v:
                _cnt += 1
            else:
                _cnt = 1
                p_v = v
                continue
            
            if _cnt == 4:
                return True

    return False

def explosion():
    
    bombs = [0, 0, 0]
    marbles = get_marbles()

    marbles = list(marbles)

    p_v = marbles[0]
    _cnt = 1
    after_marbles = deque()
    after_marbles.append(p_v)

    for i in range(1, len(marbles)):
        v = marbles[i]
        

        # 둘의 번호가 같다면?
        if v == p_v:
            _cnt += 1
        # 둘의 번호가 틀리다면?
        else:
            # 같은 번호가 4개 이상 중복되었다면?
            if _cnt >= 4:
                bombs[p_v - 1] += _cnt
                for _ in range(_cnt):
                    after_marbles.pop()

            p_v = v
            _cnt = 1
        
        after_marbles.append(v)
    
    # 같은 번호가 4개 이상 중복된 경우 => 모든 구슬이 같은 구슬인 경우
    if _cnt >= 4:
        bombs[p_v - 1] += _cnt
        for _ in range(_cnt):
            after_marbles.pop()

    move(after_marbles)
    
    return bombs

def get_marbles():
    # 현재 구슬 가져오기.
    marbles = deque()
    lengths = []
    for i in range(1, n):
        lengths.append(i)
        lengths.append(i)

    lengths.append(n - 1)

    d = 2
    r, c = s_r, s_c

    for _len in lengths:
        
        for _ in range(_len):
            r = r + dr[d]
            c = c + dc[d]
            if grid[r][c] > 0:
                marbles.append(grid[r][c])

        if d == 0: d = 2
        elif d == 1: d = 3
        elif d == 2: d = 1
        elif d == 3: d = 0

    return marbles



def move(marbles):
    global grid
    '''
        구슬의 이동
    '''
    grid = [[0 for _ in range(n)] for _ in range(n)]
    d = 2
    r, c = s_r, s_c
    

    lengths = []
    for i in range(1, n):
        lengths.append(i)
        lengths.append(i)

    lengths.append(n - 1)

    r, c = s_r, s_c
    d = 2
    is_check = False
    for _len in lengths:

        for _ in range(_len):
            r = r + dr[d]
            c = c + dc[d]
            if marbles:
                v = marbles.popleft()
                grid[r][c] = v
            else:
                is_check = True
                break

        if d == 0: d = 2
        elif d == 1: d = 3
        elif d == 2: d = 1
        elif d == 3: d = 0

        if is_check:
            break

if __name__ =="__main__":
    n, m = map(int ,input().split())
    s_r, s_c = n // 2, n // 2

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    grid = [list(map(int, input().split())) for _ in range(n)]

    magic_order = []

    for _ in range(m):
        d, s = map(int, input().split())
        magic_order.append((d - 1, s))

    res = [0, 0, 0]
    for i in range(m):
        r1, r2, r3 = magic(magic_order[i])
        res[0] += r1
        res[1] += r2
        res[2] += r3
    
    print(res[0] * 1 + res[1] * 2 + res[2] * 3)
