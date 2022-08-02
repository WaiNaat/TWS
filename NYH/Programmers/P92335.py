import math

def solution(n, k):
    '''
        - 0P0처럼 소수 양쪽에 0이 있는 경우
        - P0처럼 소수 오른쪽에만 0이 있고 
        왼쪽에는 아무것도 없는 경우
        - 0P처럼 소수 왼쪽에만 0이 있고 
        오른쪽에는 아무것도 없는 경우
        - P처럼 소수 양쪽에 아무것도 없는 경우
        단, P는 각 자릿수에 0을 포함하지 않는 소수입니다

        1. k 진수로 변환
        2. 0이 아닌 숫자를 찾는다.
    '''
    digits = create_k_binary(n, k)
    _cnt = 0

    idx = 0
    while idx < len(digits):
        if digits[idx] != "0":
            idx, val = search(idx, digits)
            if isPrime(val):
                _cnt += 1
        else:
            idx +=1    
    
    return _cnt

def create_k_binary(n, k):
    numbers = ""
    while n > 0:
        div = n // k
        mod = n % k
        n = div
        numbers += str(mod)
    numbers = list(numbers)
    numbers.reverse()
    return numbers


def search(idx, digits):
    length = len(digits)
    
    s = idx

    while idx < length and digits[idx] != "0":
        idx += 1
    
    end = idx
    val = int("".join(digits[s:end]))

    return [idx, val]

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

n = 437674
k = 3
print(solution(n, k))
n = 110011
k = 10
print(solution(n, k))