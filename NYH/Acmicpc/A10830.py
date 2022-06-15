import sys

'''
    행렬의 특성 : A^4 = A^2 * A^2
'''
def input():
    return sys.stdin.readline().rstrip()

def solution(matrix, limit):
    return sub_ploblem(matrix, limit)

def sub_ploblem(matrix, limit):
    if limit == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= 1000

        return matrix

    elif limit == 2:
        return div(matrix, matrix)
        
    if limit % 2 == 0:
        divide = sub_ploblem(matrix, limit // 2)
        return div(divide, divide)

    elif limit % 2 != 0:
        divide = sub_ploblem(matrix, limit // 2)
        return div(
            div(divide, divide), matrix
        )


def div(matrix, origin_matrix):
    length = len(matrix)
    result = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            val = 0
            for t in range(length):
                val += matrix[i][t] * origin_matrix[t][j]
            result[i][j] = val % 1000

    return result

if __name__=="__main__":
    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for sol in solution(matrix, B):
        print(" ".join(map(str,sol)))