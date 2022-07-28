import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def solv():
    global parent
    max_num = set_area_num()

    parent = [i for i in range(max_num)]
    candidate_bridge = set_candidate_bridge()

    print(kruskal(candidate_bridge,max_num))
def kruskal(candidate_bridge, max_num):
    bridge_count = 0
    length = 0

    for a,b,c in candidate_bridge:
        if not is_same_parent(a,b):
            union(a,b)
            bridge_count += 1
            length += c
            if bridge_count == max_num-3:
                return length
    return -1

def find(target):
    global parent
    if parent[target] == target:
        return target
    parent[target] = find(parent[target])
    return parent[target]

def union(a,b):
    global parent
    a = find(a)
    b = find(b)

    if a != b:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

def is_same_parent(a,b):
    return find(a) == find(b)

def set_candidate_bridge():
    candidate_bridge = set()
    for x,y,d in edges:
        start = board[x][y]
        length = 0
        while True:
            x += dx[d]
            y += dy[d]
            if boundaray_validator(x,y):
                end = board[x][y]
                if end != 0:
                    if start != end and length >= 2:
                        candidate_bridge.add((start,end,length))
                    break
                length += 1
            else:
                break

    candidate_bridge = sorted(candidate_bridge, key=lambda x:x[2])
    return candidate_bridge
def set_area_num():
    num = 2
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                bfs(x,y,num)
                num += 1
    return num
def bfs(sx,sy,num):
    global board,edges
    q = deque([(sx,sy)])
    board[sx][sy] = num

    while q:
        x,y = q.pop()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if boundaray_validator(nx,ny):
                if board[nx][ny] == 1:
                    board[nx][ny] = num
                    q.appendleft((nx,ny))
                elif board[nx][ny] == 0:
                    edges.append((x,y,d))
def boundaray_validator(x,y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True


if __name__=="__main__":
    '''
        0 바다
        1 땅
        다리의 양 끝은 
        섬과 인접한 바다 위에 있어야 한다.
        다리의 길이는 2 이상이다.

    '''
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    edges = []
    solv()

    

            




