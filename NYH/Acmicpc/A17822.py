import sys


'''
    i 번째 원판에 적힌 j번째 수의 위치 (i, j)
'''
def input():
    return sys.stdin.readline().rstrip()

def remove_circle():
    is_check = False
    same = [[False for _ in range(m)]] + [[False for _ in range(m)] for _ in range(n)]
    for c in range(1, n + 1):

        for num in range(m):
            if circle[c][num] == 0:
                continue

            if c == 1:
                if num == 0:
                    # 원판 내부 정수 비교
                    if circle[c][num] == circle[c][num + 1]:
                        same[c][num], same[c][num + 1] = True, True
                    # 원판 내부 정수 비교
                    if circle[c][-1] == circle[c][num]:
                        same[c][num], same[c][-1] = True, True
                    # 원판 1과 2 비교
                    if circle[c][num] == circle[c + 1][num]:
                        same[c][num], same[c + 1][num] = True, True

                elif num == m - 1:
                    # 원판 내부 정수 비교
                    if circle[c][num] == circle[c][0]:
                        same[c][num], same[c][0] = True, True
                    # 원판 내부 정수 비교
                    if circle[c][num] == circle[c][num - 1]:
                        same[c][num], same[c][num - 1] = True, True
                    # 원판 1과 2 비교
                    if circle[c][num] == circle[c + 1][num]:
                        same[c][num], same[c + 1][num] = True, True
                else:
                    if circle[c][num] == circle[c][num - 1]:
                        same[c][num], same[c][num - 1] = True, True

                    if circle[c][num] == circle[c][num + 1]:
                        same[c][num], same[c][num + 1] = True, True

                    if circle[c][num] == circle[c + 1][num]:
                        same[c][num], same[c + 1][num] = True, True

            elif c == n:
                if num == 0:
                    if circle[c][num] == circle[c][num + 1]:
                        same[c][num], same[c][num + 1] = True, True

                    if circle[c][-1] == circle[c][num]:
                        same[c][num], same[c][-1] = True, True

                    if circle[c][num] == circle[c - 1][num]:
                        same[c][num], same[c - 1][num] = True, True

                elif num == m - 1:
                    # 원판 내부 정수 비교
                    if circle[c][num] == circle[c][0]:
                        same[c][num], same[c][0] = True, True

                    if circle[c][num] == circle[c][num - 1]:
                        same[c][num], same[c][num - 1] = True, True
                    # 원판 비교
                    if circle[c][num] == circle[c - 1][num]:
                        same[c][num], same[c - 1][num] = True, True
                else:
                    if circle[c][num] == circle[c][num - 1]:
                        same[c][num], same[c][num - 1] = True, True

                    if circle[c][num] == circle[c][num + 1]:
                        same[c][num], same[c][num + 1] = True, True
                        
                    if circle[c][num] == circle[c - 1][num]:
                        same[c][num], same[c - 1][num] = True, True

            else:
                if num == 0:
                    if circle[c][num] == circle[c][num + 1]:
                        same[c][num], same[c][num + 1] = True, True

                    if circle[c][-1] == circle[c][num]:
                        same[c][num], same[c][-1] = True, True

                    if circle[c][num] == circle[c + 1][num]:
                        same[c][num], same[c + 1][num] = True, True

                    if circle[c][num] == circle[c - 1][num]:
                        same[c][num], same[c - 1][num] = True, True

                elif num == m - 1:
                    # 원판 내부 정수 비교
                    if circle[c][num] == circle[c][0]:
                        same[c][num], same[c][0] = True, True

                    if circle[c][num] == circle[c][num - 1]:
                        same[c][num], same[c][num - 1] = True, True

                    # 원판 비교
                    if circle[c][num] == circle[c + 1][num]:
                        same[c][num], same[c + 1][num] = True, True

                    if circle[c][num] == circle[c - 1][num]:
                        same[c][num], same[c - 1][num] = True, True

                else:
                    if circle[c][num] == circle[c][num - 1]:
                        same[c][num], same[c][num - 1] = True, True

                    if circle[c][num] == circle[c][num + 1]:
                        same[c][num], same[c][num + 1] = True, True

                    if circle[c][num] == circle[c + 1][num]:
                        same[c][num], same[c + 1][num] = True, True

                    if circle[c][num] == circle[c - 1][num]:
                        same[c][num], same[c - 1][num] = True, True

    for row in range(1, n + 1):
        for col in range(m):
            # 수를 지운다.
            if same[row][col]:
                is_check = True
                circle[row][col] = 0


    return is_check


def rotate_circle(d, idx):
    if d == 0:
        # d == 0
        temp = circle[idx][-1]
        circle[idx] = circle[idx][:-1]
        circle[idx].insert(0, temp)
    elif d == 1:
        temp = circle[idx][0]
        circle[idx] = circle[idx][1:]
        circle[idx].append(temp)

if __name__ =="__main__":
    n, m, t = map(int,input().split())
    circle = [[0 for _ in range(m)]] + [list(map(int,input().split())) for _ in range(n)]
    rotates = []
    for _ in range(t):
        x, d, k = map(int, input().split())
        rotates.append((x, d, k))

    for rotate in rotates:
        # 회전
        x, d, k = rotate
        for num in range(1, n + 1):
            # 원판이 배수이면 
            if num % x == 0:
                # k번 회전
                for _ in range(k):
                    rotate_circle(d, num)

        # 회전 후
        is_check = remove_circle()

        if not is_check:
            _sum = 0
            _cnt = 0
            for r in range(1, n + 1):
                for c in range(m):
                    if circle[r][c] != 0:
                        _sum += circle[r][c]
                        _cnt +=1
            if _cnt == 0:
                continue
            
            avg = _sum / _cnt
            
            for r in range(1, n + 1):
                for c in range(m):
                    if circle[r][c] != 0 :
                        if circle[r][c] > avg:
                            circle[r][c] -= 1
                        elif circle[r][c] < avg:
                            circle[r][c] += 1

    res = 0
    for i in range(1, n + 1):
        res += sum(circle[i])
    print(res)