import sys
'''
    피보나치는 행렬로도 풀 수 있다네요.
'''
def input():
    return sys.stdin.readline().rstrip()

def solution(N):
    matrix = [
        [1, 1],
        [1, 0]
    ]
    return sub_ploblem(N, matrix)

def sub_ploblem(N, matrix):
    if N == 1:  
        return matrix

    if N % 2 != 0:
        return div(sub_ploblem(N - 1, matrix), matrix)

    elif N % 2 == 0:
        return sub_ploblem(N // 2, div(matrix, matrix))


def div(l_matrix, r_matrix):
    length = len(l_matrix)
    result = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for t in range(length):
                result[i][j] += (l_matrix[i][t] * r_matrix[t][j])
            result[i][j] %= INF   

    return result

if __name__ == "__main__":
    N = int(input())
    INF = 1000000007
    print(solution(N)[0][1])