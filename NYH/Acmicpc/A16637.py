import sys

def input():
    return sys.stdin.readline().rstrip()


def calc(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2



def dfs(cnt, val):
    global res

    if cnt >= len(op):
        res = max(res, val)
        return

    dfs(cnt + 1, calc(val, num[cnt + 1], op[cnt]))

    if cnt + 1 < len(op):
        dfs(cnt + 2, calc(val, calc(num[cnt + 1], num[cnt + 2], op[cnt + 1]),  op[cnt]))
    


if __name__ =="__main__":
    '''
        괄호 안에는 연산자가 하나만 들어간다.
    '''
    n = int(input())
    express = input()
    express = list(map(str, express))

    num, op = [], []
    res = -1e9

    for i in range(n):
        if i % 2 == 0:
            num.append(int(express[i]))
        else:
            op.append(express[i])
    
    dfs(0, num[0])
    print(res)
    

    