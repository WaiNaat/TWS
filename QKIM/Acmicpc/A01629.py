import sys
sys.setrecursionlimit(10 ** 6)
# function
def pow_mod(base, exponent, divisor):
	'''
	a^b는 다음과 같이 쪼갤 수 있다.
	a^{b/2} * a^{b/2} (b가 짝수)
	a^{(b-1)/2} * a^{(b-1)/2} * a (b가 홀수)

	나머지 연산은 다음이 성립한다.
	(x * y) % z = (x%z * y%z) % z
	'''
	if exponent == 0: return 1
	pow_half = pow_mod(base, exponent // 2, divisor)
	if exponent % 2 == 0:
		return (pow_half * pow_half) % divisor
	else:
		return (pow_half * pow_half * base) % divisor

# input
a, b, c = map(int, input().split())
# process & output
print(pow_mod(a, b, c))