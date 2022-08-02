import math
def solution(fees, records):
    '''
        주차요금 계산식
        기본시간 180분
        기본 요금 5000원
        단위시간 10분당 600 원

        time < 180 => result : 5000
        time >= 180
        => math.ceil((time - 180) / 10) * 600

        입 출차 여부를 어떻게?
        23:59에는 자동으로 출차된다.
        1. 중간 시간 관리용 딕셔너리
        2. 총 시간 관리용 딕셔너리
    '''
    time_d = {}
    record_time_d = {}

    for record in records:
        time, car_num, exit_check = record.split(" ")

        if exit_check == "OUT":
            s_time = time_d.pop(car_num)
            minute = calc_time(s_time, time)
            
            try:
                record_time_d[car_num] += minute
            except:
                record_time_d[car_num] = minute

        elif exit_check == "IN":
            time_d[car_num] = time
        
    # 입차된 차가 남아있다면?
    for car_num in time_d.keys():
        s_time = time_d[car_num]
        e_time = "23:59"
        minute = calc_time(s_time, e_time)

        try:
            record_time_d[car_num] += minute
        except:
            record_time_d[car_num] = minute

    res = []
    for key in sorted(record_time_d.keys()):
        cost = calc_cost(record_time_d[key], fees)
        res.append(cost)

    return res

def calc_time(start_time, end_time):
    s_h, s_m = map(int,start_time.split(":"))
    e_h, e_m = map(int,end_time.split(":"))

    minute = (e_h - s_h) * 60
    minute = minute + e_m - s_m

    return minute

def calc_cost(time, fees):
    default_time = fees[0]
    default_cost = fees[1]
    unit_time = fees[2]
    unit_cost = fees[3]

    if time < default_time:
        return default_cost
    
    elif time >= default_time:
        cost = math.ceil((time - default_time) / unit_time) * unit_cost
        return cost + default_cost



fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))