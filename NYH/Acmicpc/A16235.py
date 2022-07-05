import sys

def input():
    return sys.stdin.readline().rstrip()

def sub_ploblem():
    global count
    # 봄, 여름
    for r in range(n):
        for c in range(n):
            if trees[r][c]:
                for i in range(len(trees[r][c])):
                    if board[r][c] - trees[r][c][i] < 0:
                        dead_tree = trees[r][c][i:]
                        for age in dead_tree:
                            board[r][c] += age // 2
                        trees[r][c] = trees[r][c][:i]
                        count -= len(dead_tree)
                        break
                    else:
                        board[r][c] -= trees[r][c][i]
                        trees[r][c][i] += 1


    # 가을        
    for r in range(n):
        for c in range(n):
            if trees[r][c]:
                for age in trees[r][c]:
                    if age % 5 == 0:
                        for dir in dirs:
                            dr, dc = r + dir[0], c + dir[1]
                            # 칸을 넘는다면?
                            if dr < 0 or dr >= n or dc < 0 or dc >=n:
                                continue
                            trees[dr][dc].insert(0, 1)
                            count += 1

    # 겨울
    for row in range(n):
        for col in range(n): 
            board[row][col] += feed[row][col]
    return

if __name__=="__main__":
    
    n, m, k = map(int, input().split())
    # 각 땅에 존재하는 양분 배열
    board = [[5 for _ in range(n)] for _ in range(n)]
    # 나무 배열
    trees = [[[] for _ in range(n)] for _ in range(n)]

    dirs = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1),
        (0, 1), (1, -1), (1, 0), (1, 1)
    ]

    # 겨울 마다 추가되는 양분 배열
    feed = []

    for i in range(n):
        feed.append(list(map(int,input().split())))
    
    for _ in range(m):
        r, c, age = map(int,input().split())
        trees[r - 1][c - 1].append(age)

    # 트리 정렬
    for i in range(n):
        for j in range(n):
            trees[i][j].sort()

    count = m

    for _ in range(k):
        sub_ploblem()    

    print(count)
