import sys

def input():
    return sys.stdin.readline().rstrip()


def solution(board, L):
    cnt = 0
    for row in range(N):
        arr = board[row][:]
        cnt += sub_ploblem(arr, L)

    for col in range(N):
        arr = list(zip(*board))[col]
        cnt += sub_ploblem(arr, L)
    
    return cnt

def sub_ploblem(line, L):
    visited = [False for _ in range(N)]
    for i in range(0, N - 1):
        # 값이 동일하다면?
        if line[i] == line[i+1]: continue

        # 값이 차이가 1보다 크다면?
        elif abs(line[i]-line[i+1]) > 1: return False

        # 경사면 정방향
        elif line[i] > line[i+1]:
            temp = line[i+1]
            for j in range(i + 1, i + L +1):
                if 0 <= j < N:
                    # 경사면 바닥의 높이가 같은지?
                    if temp != line[j]:
                        return False
                    # 이미 방문했는지
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False

        # 경사면 역방향
        else:
            temp = line[i]
            for j in range(i, i - L, -1):
                if 0 <= j < N:
                    # 경사면 바닥의 높이가 같은지?
                    if temp != line[j]:
                        return False
                    # 이미 방문 했는지.
                    elif visited[j]:
                        return False
                    visited[j] = True
                else:
                    return False
    return True

if __name__=="__main__":
    N, L = map(int,input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(solution(board, L))
