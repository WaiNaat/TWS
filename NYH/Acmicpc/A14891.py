import sys
from collections import deque

class Gears:
    def __init__(self, gear):
        self.gear = gear
        for i in range(4):
            gear[i] = deque(gear[i])
    
    def getLeft(self, no):
        return self.gear[no][6]
    
    def getTop(self, no):
        return self.gear[no][0]
    
    def getRight(self, no):
        return self.gear[no][2]
    
    def getBottom(self, no):
        return self.gear[no][4]

    def clock_wise(self, no):
        '''
            시계 방향
        '''
        cur = self.gear[no].pop()
        self.gear[no].appendleft(cur)

    def counter_clock_wise(self, no):
        '''
            반시계 방향
        '''
        cur = self.gear[no].popleft()
        self.gear[no].append(cur)


def input():
    return sys.stdin.readline().rstrip()

def solution():
    return


if __name__=="__main__":
    '''
        N극은 0, S극은 1
        1번 right, 2번 left 연결 관계
        2번 right, 3번 left 연결 관계
        3번 right, 4번 left 연결 관계
        서로 같은 극일때 회전하지 않는다.

        12시 방향이 S극이면 
        1번 : 1점
        2번 : 2점
        3번 : 4점
        4번 : 8점
        N극이면 모두 0 점
    '''
    
    # 톱니바퀴 객체
    gears = Gears([list(map(int, input())) for _ in range(4)])
    K = int(input())

    # 회전 톱니바퀴 번호, 회전 방향(1 : 시계, -1 : 반시계)
    rotates = [list(map(int,input().split())) for _ in range(K)]
    for cur_no, cur_rotate in rotates:
        '''
            한번 회전당 톱니바퀴는 한칸씩만 이동
            즉 회전 당시에 회전이 가능한지만 체크하면 된다.
            다만 현재 왼쪽이든 오른쪽이든 극이 같더라도
            이미 회전 배열에 들어가 있다면 해당 회전은 실시된다.
            ex) 3, -1이 입력값으로 주어졌을 때 2번 톱니바퀴와 극이 같다고 해도
            3번 회전은 실시된다. 2번 회전부터 실시되어지지 않는다.
        '''
        
        rotate = cur_rotate

        array = [[cur_no - 1, cur_rotate]]
        prev_left = gears.getLeft(cur_no - 1)
        for i in range(cur_no - 2, -1, -1):
            if prev_left == gears.getRight(i):
                break
            else:
                rotate = -rotate
                array.append([i, rotate])  
                prev_left = gears.getLeft(i)
        
        rotate = cur_rotate
        prev_right = gears.getRight(cur_no - 1)
        for i in range(cur_no, 4):
            if prev_right == gears.getLeft(i):
                break
            else:
                rotate = -rotate
                array.append([i, rotate])
                prev_right = gears.getRight(i)

        for arr in array:
            num, rotate = arr
            if rotate == 1:
                gears.clock_wise(num) 
            else:
                gears.counter_clock_wise(num)

    res = 0
    for i in range(4):
        if gears.getTop(i) == 1:
            res += (2 ** i)
    print(res)    