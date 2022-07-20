import sys

def input():
    return sys.stdin.readline().rstrip()


def move_pos(student):

    comp = shark_favorite[student]
    arr = []

    for r in range(n):
        for c in range(n):

            favor_cnt = 0
            empty_cnt = 0
            # 비어있는 칸이라면?
            if grid[r][c] == 0:
                
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]

                    # 범위를 벗어나면?
                    if nr < 0 or nc < 0 or nr >= n or nc >= n:
                        continue
                    
                    # 빈칸 이라면?
                    if grid[nr][nc] == 0:
                        empty_cnt += 1
                        continue
                
                    # 만약 비어있는 칸에 인접한 칸이 좋아하는 학생이 거주하면?
                    if grid[nr][nc] in comp:
                        favor_cnt += 1
                    

                arr.append([favor_cnt, empty_cnt, r, c])                    


    arr.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))

    return arr[0][2:]


def calc_score(favor_cnt):
    if favor_cnt == 1:
        return 1
    elif favor_cnt == 2:
        return 10
    elif favor_cnt == 3:
        return 100
    elif favor_cnt == 4:
        return 1000
    else:
        return 0

if __name__ == "__main__":

    '''
        abs(r1 - r2) + abs(c1 - c2) = 1 이면
        (r1, c1), (r2, c2) 인접.
        그냥 상 하 좌 우
        
        1. 비어있는 칸 중에서 좋아하는 학생이 
        인접한 칸에 가장 많은 칸

        2. 1을 만족하는 칸이 여러 개 이면 
        인접한 칸 중 비어있는 칸이 가장 많은 칸

        3. 2를 만족하는 칸도 여러 개인 경우에는
        행의 번호가 가장 작은 칸, 그러한 칸도 여러개이면
        열의 번호가 가장 작은 칸.
    '''
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    n = int(input())

    grid = [[0 for _ in range(n)] for _ in range(n)]

    s_num = n * n
    shark_favorite = [[] for _ in range(s_num + 1)]

    students = []
    for _ in range(s_num):
        l = list(map(int,input().split()))
        students.append(l[0])
        shark_favorite[l[0]] = l[1:]
    
    # 이동
    for student in students:
        r, c = move_pos(student)
        grid[r][c] = student

    sum_score = 0
    for r in range(n):
        for c in range(n):
            
            favor_cnt = 0

            student = grid[r][c]
            
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if nr < 0 or nc < 0 or nr >= n or nc >= n:
                    continue
                
                # 인접칸에 좋아하는 사람이 있으면?
                if grid[nr][nc] in shark_favorite[student]:
                    favor_cnt += 1

            sum_score += calc_score(favor_cnt)

    print(sum_score)

                    

