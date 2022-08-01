def solution(id_list, report, k):
    '''
        유저 별로 처리결과 메일을 받은 횟수
        만들 것
        1. k번 이상 신고당한 목록
        2. 유저별 신고한 사람 목록
        3. 한 유저가 같은 유저를 여러번 신고하면 1회로 처리
    '''
    d = {}
    d2 = {}
    res = [0 for _ in range(len(id_list))]
    for id in id_list:
        d2[id] = 0


    for val in report:
        reporter, reported = val.split(" ")

        try:
            if reported not in d[reporter]:
                d[reporter].append(reported)
                d2[reported] += 1
        except:
            d[reporter] = []
            d[reporter].append(reported)
            d2[reported] += 1
    
    
    # id가 k번 이상 신고 당했다면
    reported_id = []
    for key in d2.keys():
        if d2[key] >= k:
            reported_id.append(key)
    
    
    idx = -1
    for key in d.keys():
        idx = id_list.index(key)

        # 만약 딕셔너리의 val 값이 신고되서 정지된 id 이면?
        for val in d[key]:
            if val in reported_id:
                res[idx] += 1

    return res

if __name__=="__main__":
    '''
        id_list : 사용자 리스트
        report : 사용자 id + " " + 신고한 id
    '''
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    print(solution(id_list, report, k))

    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    print(solution(id_list, report, k))