import sys

def input():
    return sys.stdin.readline().rstrip()

def get_papers(r, c):
    '''
        (r, c)에서 
        어떤 색종이를 쓸 수 있는지를
        반환한다.
    '''
    sub_paper = []
    for n in range(1, 6):
        for x in range(r, r + n):
            for y in range(c, c + n):
                if x < 0 or x >= 10 or y < 0 or y >= 10 or grid[x][y] == 0:
                    return sub_paper

        sub_paper.append(n)

    return sub_paper


def fill_grid(r, c, t, val):
    '''
        특정한 번호의
        색종이를 채워넣는다.
    '''
    for i in range(r, r + t):
        for j in range(c, c + t):
            grid[i][j] = val

def dfs(temp):
    global res
    if temp == 0:
        res = min(res, 25 - sum(papers[1:]))
        return
    
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1:
                sub_paper = get_papers(i, j)

                for k in range(len(sub_paper) -1, -1, -1):
                    num = sub_paper[k]

                    if papers[num] > 0:
                        papers[num] -= 1
                        fill_grid(i, j, num, 0)
                        dfs(temp - (num ** 2))
                        fill_grid(i, j, num, 1)
                        papers[num] += 1
                return


if __name__=="__main__":
    grid = [list(map(int, input().split())) for _ in range(10)]

    papers = [0, 5, 5, 5, 5, 5]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    _cnt = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1:
                _cnt += 1
    
    res = 25

    dfs(_cnt)
    print( -1 if res == 25 else res)