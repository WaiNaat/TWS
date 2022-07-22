import sys
from copy import deepcopy

def input():
    return sys.stdin.readline().rstrip()

def fish_move(n, fish):
    fish_temp = deepcopy(fish)
    for i in range(n):
        if fish[i]:
            for j in range(len(fish[i])):
                if i + 1 < len(fish):
                    if j < len(fish[i + 1]):
                        if fish[i + 1][j]:
                            if fish[i][j] > fish[i + 1][j]:
                                diff = (fish[i][j] - fish[i + 1][j]) // 5
                                fish_temp[i][j] -= diff
                                fish_temp[i + 1][j] += diff
                            elif fish[i][j] < fish[i + 1][j]:
                                diff = (fish[i + 1][j] - fish[i][j]) // 5
                                fish_temp[i][j] += diff
                                fish_temp[i + 1][j] -= diff

                if j + 1 < len(fish[i]):
                    if fish[i][j] > fish[i][j + 1]:
                        diff = (fish[i][j] - fish[i][j + 1]) // 5
                        fish_temp[i][j] -= diff
                        fish_temp[i][j + 1] += diff
                    elif fish[i][j] < fish[i][j + 1]:
                        diff = (fish[i][j + 1] - fish[i][j]) // 5
                        fish_temp[i][j] += diff
                        fish_temp[i][j + 1] -= diff
    return fish_temp


def make_line():
    blank_idx = 0
    for i in range(n):
        if len(fish[i]) > 1:
            temp = fish[i]
            fish[i] = []
            for k in temp:
                fish[blank_idx].append(k)
                blank_idx += 1


if __name__ =="__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    fish = [[] for _ in range(n)]
    for i in range(n):
        fish[i].append(a[i])

    cnt = 1
    while True:
        min_n = sys.maxsize
        for i in range(len(fish)):
            min_n = min(fish[i][0], min_n)
        for i in range(len(fish)):
            if fish[i][0] == min_n:
                fish[i][0] += 1

        fish[1].append(fish[0][0])
        fish[0] = []

        flag = 0
        while True:
            for i in range(len(fish)-1, 0, -1):
                if len(fish[i]) > 1:
                    if len(fish[i]) > len(fish) - i - 1:
                        flag = 1
                        break
                    for j in range(i + 1, n):
                        if fish[j]:
                            for v, idx in zip(fish[i], range(j, j + len(fish[i]) + 1)):
                                fish[idx].append(v)
                            break
                    fish[i] = []
            if flag == 1:
                break

        fish = fish_move(n, fish)

        make_line()

        left, right = fish[:n//2], fish[n//2:]
        n_left = left[-1::-1]
        for l, r in zip(n_left, right):
            r.append(l[0])

        left, right = right[:n//4], right[n//4:]
        for _ in range(2):
            left = list(zip(*left[::-1]))
        for l, r in zip(left, right):
            for ll in l:
                r.append(ll)

        right = fish_move(n//4, right)

        fish = [[] for _ in range(n)]
        for i in range(len(right)):
            fish[-i-1] = right[len(right) - i -1]
        make_line()

        max_n, min_n = 0, sys.maxsize
        for f in fish:
            max_n = max(f[0], max_n)
            min_n = min(f[0], min_n)

        if max_n - min_n <= k:
            print(cnt)
            break

        cnt += 1