import sys

def input():
    return sys.stdin.readline().rstrip()
    
def is_check(x):
    for i in range(x):
        # 열 - 열 == 행 - 행 ? row[x] == row[i] 열 == 열 ?
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def sub_ploblem(x):
    global ans

    # 모든 queen을 넣었을 때
    if x == N:
        ans += 1
        return
    
    for i in range(N):
        row[x] = i
        if is_check(x):
            sub_ploblem(x + 1)
    

if __name__ =="__main__":
    N = int(input())
    ans = 0
    row = [0 for _ in range(N)]
    sub_ploblem(0)
    print(ans)