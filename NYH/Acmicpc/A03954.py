import sys
def input():
    return sys.stdin.readline().rstrip()

def loop():
    global pid, pointer, code_idx, mem_size, code_size, input_size
    c = program[pid]

    if c == '-':
        mem[pointer] = 255 if (mem[pointer] - 1) < 0 else mem[pointer] - 1
    elif c == '+':
        mem[pointer] = 0 if (mem[pointer] + 1) > 255 else mem[pointer] + 1
    elif c == '<':
        pointer = mem_size - 1 if pointer - 1 == -1 else pointer - 1 
    elif c == '>':
        pointer = 0 if pointer + 1 == mem_size else pointer + 1
    elif c == ']':
        if mem[pointer] != 0:
            # 현재 위치를 닫는 괄호 위치로 점프
            pid = bracket[pid]
    elif c == '[':
        if mem[pointer] == 0:
            # 현재 위치를 여는 괄호 위치로 점프
            pid = bracket[pid]
    elif c == '.':
        pass
    elif c == ',':
        mem[pointer] = 255 if code_idx == input_size else ord(text[code_idx])
        code_idx += 1

    pid += 1

    return

if __name__ =="__main__":
    t = int(input())
    res = []
    for _ in range(t):
        pointer, code_idx = 0, 0
        
        mem_size, code_size, input_size = map(int, input().split())
        program = input()
        text = input()
        stack = []
        mem = [0] * mem_size
        bracket = [0] * code_size

        for i in range(code_size):
            code = program[i]

            if code == '[':
                stack.append(i)
            elif code ==']':
                temp = stack[-1]
                # 여는 괄호에 닫는 괄호
                bracket[i] = temp
                # 닫는 괄호에 여는 괄호
                bracket[temp] = i
                stack.pop()

        # 명령어 위치
        pid = 0
        # 반복 횟수
        cnt = 0
        while cnt <= 50000000 and pid < code_size:
            cnt += 1
            loop()

        if pid == code_size:
            print("Terminates")
        else:
            # 무한 루프 발생
            maxpid = pid
            minpid = pid

            while cnt > 0:
                loop()
                maxpid = max(maxpid, pid)
                minpid = min(minpid, pid)
                cnt -= 1
                
            
            print("Loops", minpid - 1, maxpid)
