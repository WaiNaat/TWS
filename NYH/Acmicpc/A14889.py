import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

def solution(board):
    global min_team
    '''
        같은 팀에 속하면
        s(i, j) + s(j, i)
        (1, 3), (1, 4), (2, 3)
    '''

    for comb in combinations([i for i in range(N)] , N // 2):
        visited = [False] * len(board)
        start = []
        for visit in comb:
            visited[visit] = True
            start.append(visit)
        
        min_team = min(sub_ploblem(start, board, visited), min_team)

def sub_ploblem(start, board, visited):

    link = []
    for i in range(len(visited)):
        if not visited[i]:
            link.append(i)

    start_result = 0
    for comb in combinations(start, 2):
        start_result += board[comb[0]][comb[1]] 
        start_result += board[comb[1]][comb[0]]
    
    link_result = 0
    for comb in combinations(link, 2):
        link_result += board[comb[0]][comb[1]] 
        link_result += board[comb[1]][comb[0]]

    return abs(link_result - start_result)

if __name__ =="__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    min_team = 1e9
    solution(board)
    print(min_team)
