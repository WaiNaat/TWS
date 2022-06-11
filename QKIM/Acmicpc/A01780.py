import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
# function
def cut(row, col, size):
	'''
	paper[row][col]부터 시작하는 size*size 크기의 종이를 확인.
	모두 같은 수면 cnt 배열을 업데이트하고
	아니면 9등분해서 재귀함.
	'''
	isAll1 = isAll0 = isAllM1 = True
	for r in range(row, row + size):
		for c in range(col, col + size):
			if paper[r][c] == 0: isAll1 = isAllM1 = False
			elif paper[r][c] == 1: isAllM1 = isAll0 = False
			else: isAll1 = isAll0 = False
		if not isAll1 and not isAll0 and not isAllM1: break
	
	if isAllM1: cnt[0] += 1
	elif isAll0: cnt[1] += 1
	elif isAll1: cnt[2] += 1
	else:
		size //= 3
		for i in range(3):
			for j in range(3):
				cut(row + i * size, col + j * size, size)

# input
n = int(input())
paper = [tuple(map(int, input().split())) for _ in range(n)]
# process & output
cnt = [0, 0, 0]
cut(0, 0, n)
print(*cnt)