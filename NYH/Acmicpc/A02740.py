import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(A, B):

    A_row = len(A)
    B_col = len(B[0])

    result = [[0 for _ in range(B_col)] for _ in range(A_row)]

    for i in range(A_row):
        for j in range(B_col):
            result[i][j] += div(A, B, (i, j))

    return result

def div(A, B, pos):
    
    val = 0
    for i in range(len(A[0])):
        val += A[pos[0]][i] * B[i][pos[1]]
    return val

if __name__ == "__main__":
    N, M = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    M, K = map(int, input().split())

    for _ in range(M):
        B.append(list(map(int, input().split())))

    for sol in solution(A, B):
        print(" ".join(map(str, sol)))
