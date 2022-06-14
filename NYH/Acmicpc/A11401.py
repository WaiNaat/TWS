import sys
'''
    이항 계수
    n, k

    n! / k! * (n -k)! (0 <= k <= n)
    0 (k < 0)
    0 (k > n)

    n C k % p = n! % p * (k! * (n-k)!) ^ (p - 2) % p   
    어지럽다
'''
def input():
    return sys.stdin.readline().rstrip()

def factorial(n):
    fact = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % INF

    return fact[n]

def divide(num, mod):
    if mod == 0:
        return 1
    elif mod % 2 != 0:
        return divide(num , mod - 1) * num % INF
    half = divide(num, mod // 2)

    return (half * half) % INF
    
    

def solution(n, k):
    num_n = factorial(n)
    num_k = (factorial(n - k) * factorial(k)) % INF
    return (num_n * divide(num_k, INF - 2) % INF) 


if __name__ =="__main__":
    INF = 1000000007
    n, k = map(int, input().split())
    print(solution(n, k))