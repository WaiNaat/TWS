import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# function
def quadTree(row, col, length):
	'''
	img[row][col] 부터 시작해서 length^2 개의 점을 본다.
	base case: 전부 0 또는 1이면 그대로 반환.
	recursive step:
		좌상, 우상, 좌하, 우하 위치로 각각 재귀 후
		네 가지 결과를 괄호로 묶어서 반환.
	'''
	isAll0 = isAll1 = True
	for r in range(row, row + length):
		for c in range(col, col + length):
			if img[r][c] == '1': isAll0 = False
			else: isAll1 = False
	
	if isAll0: return '0'
	elif isAll1: return '1'

	length //= 2
	ret = ['(']
	ret.append(quadTree(row, col, length))
	ret.append(quadTree(row, col + length, length))
	ret.append(quadTree(row + length, col, length))
	ret.append(quadTree(row + length, col + length, length))
	ret.append(')')
	return "".join(ret)

# input
n = int(input())
img = [input().rstrip() for _ in range(n)]
# process & output
print(quadTree(0, 0, n))