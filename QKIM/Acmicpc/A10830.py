import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
# functions
def product(a, b, size):
	'''
	크기가 size*size인 두 행렬 a와 b의 곱 계산 후 1000으로 나눈 나머지 반환
	'''
	ret = [[0 for _ in range(size)] for _ in range(size)]
	for i in range(size):
		for j in range(size):
			ret[i][j] = sum([a[i][k] * b[k][j] for k in range(size)]) % 1000
	return ret

def pow(m, exponent, size):
	'''
	a^b = 
		a^(b/2) * a^(b/2)  (b가 짝수)
		a^((b-1)/2) * a^((b-1)/2) * a  (b가 홀수)

	(a * b) % c = (a%c * b%c) % c
	'''
	# base case
	if exponent == 1:
		for i in range(n):
			for j in range(n):
				m[i][j] %= 1000
		return m
	elif exponent == 2:
		return product(m, m, size)
	# recursive step
	if exponent % 2 == 0:
		half = pow(m, exponent // 2, size)
		return product(half, half, size)
	else:
		half = pow(m, (exponent - 1) // 2, size)
		return product(product(half, half, size), m, size)

# input
n, b = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]
# process
result = pow(m, b, n)
# output
for line in result:
	print(*line)