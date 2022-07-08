import sys
def input():
    return sys.stdin.readline().rstrip()

def calc_r(A):

    max_len = -1

    for r in range(len(A)):
        grid = []
        s = set(A[r])

        for v in s:
            if v:
                grid.append([v, A[r].count(v)])

        grid.sort(key=lambda x:(x[1], x[0]))
        len_grid = len(grid)
        
        # 50 * (key, value) = 100
        if len(grid) > 50:
            len_grid = 50

        temp = []

        for i in range(len_grid):
            temp.extend(grid[i])

        max_len = max(len(temp), max_len)
        A[r] = temp
    
    for row in A:
        while len(row) < max_len:
            row.append(0)

if __name__=="__main__":
    R, C, K = map(int,input().split())

    A = [list(map(int, input().split())) for _ in range(3)]

    r, c = R - 1, C - 1
    is_True = False
    for s in range(101):
        
        try:
            if A[r][c] == K:
                print(s)
                is_True = True
                break
        except:
            pass

        cur_r = len(A)
        cur_c = len(A[0])

        if cur_r >= cur_c:
            calc_r(A)
        else:
            # 행 => 열
            A = list(zip(*A))
            calc_r(A)
            # 열 => 행
            A = list(zip(*A))
    
    if not is_True:
        print(-1)


    