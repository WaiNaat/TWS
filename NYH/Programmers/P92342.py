from itertools import combinations_with_replacement

def solution(n, info):
    '''
        라이언이 우승할 수 없는 경우 [-1] 반환
        어피치 우승 경우
        1. 비긴다
        2. 어피치가 점수가 높다

        라이언 우승 경우
        1. 라이언이 점수가 높다.

        화살 점수 채점 기준

        1. k점에 화살이 동일하게 꽂히면 => 어피치가 획득
        2. k점에 어피치가 화살을 많이 꽂으면 => 어피치가 획득
        3. k점에 라이언이 화살을 많이 꽂으면 => 라이언이 획득

        라이언이 가장 큰 점수차이로 우승하는 
        화살 배열을반환

        info 배열은 어피치가 맞춘 화살
        info 배열의 i번째 원소는 과녁의 10 - i 점을 
        맞힌 화살 개수
        ex) [2,1,1,1,0,0,0,0,0,0,0]
        => 10점 2개
        => 9점 1개
        => 8점 1개
        => 7점 1개

        화살로 어피치의 점수를 뺏는게 좋은가
        화살로 어피치의 점수를 인정하고 내 점수를 가져오는게 좋은가?
        라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우,
        가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
        => 완탐
    '''
    max_val = 0
    answer = [-1]

    for comb in list(combinations_with_replacement(range(0, 11), n)):
        # p1 어피치, p2 라이언
        p1, p2 = 0, 0
        result = [0] * 11

        for val in comb:
            result[10 - val] += 1

        for i in range(11):

            if info[i] > 0 and info[i] >= result[i]:
                p1 += 10 - i
            elif result[i] > 0 and info[i] < result[i]:
                p2 += 10 - i

        if p2 - p1 > 0:
            if p2 - p1 > max_val:
                max_val = p2 - p1
                answer = result

    return answer

n = 9
info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(n, info))
