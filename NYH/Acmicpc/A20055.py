import sys 

def input():
    return sys.stdin.readline().rstrip()


if __name__=="__main__":
    n, k = map(int ,input().split())

    belt = list(map(int, input().split()))

    robot = []

    step = 1

    while True:
        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한칸 회전
        last = belt[-1]
        belt = belt[:-1]
        belt.insert(0, last)

        remove_n = False

        for i in range(len(robot)):
            robot[i] = robot[i] + 1
            if robot[i] == n - 1:
                remove_n = True

        if remove_n:
            robot.remove(n - 1)
        # 2. 가장 먼저 벨트에 올라간 로봇부터, 
        # 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 
        # 만약 이동할 수 없다면 가만히 있는다.

        # 로봇이 존재하면?
        if robot:
            remove_n = False
            for i in range(len(robot)):
                pos = robot[i]
                # 내구도가 1 이상 남고, 로봇이 없어야함
                if belt[pos + 1] >= 1 and pos + 1 not in robot:
                    robot[i] = pos + 1
                    belt[pos + 1] -= 1
                
                if robot[i] == n- 1:
                    remove_n = True
            
            if remove_n:
                robot.remove(n - 1)

        # 3. 올리는 위치 칸의 내구도가 0이 아니라면 올리는 위치에 로봇을 올린다.
        if belt[0] > 0:
            belt[0] -= 1
            robot.append(0)

        # 내구도가 0인 칸의 개수가 k개 이상이라면 과정 종료
        _cnt = belt.count(0)

        if _cnt >= k:
            break

        step += 1
    print(step)
        