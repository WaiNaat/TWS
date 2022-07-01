import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def solution(N, man, B, C):
    '''
    최소 N명의 총감독관이 필요
    '''
    viewer = N

    if N == 1:
        man -= B
        return viewer + int(math.ceil(man / C))

    
    for i in range(N):
        man[i] -= B
        if man[i] > 0:
            viewer += int(math.ceil(man[i] / C))
    
    return viewer

if __name__=="__main__":
    N = int(input())
    if N == 1:
        man = int(input())
    else:
        man = list(map(int, input().split()))
    B, C = map(int, input().split())
    print(solution(N, man, B, C))