import sys
input = sys.stdin.readline

'''
opt(i, j)를 0번~i번 물건들을 최대무게 j인 배낭에 담을 때 최대 가치라 하면
opt(i, j) = 
	opt(i-1, j)   (i번째 물건을 넣지 않음)
	opt(i-1, j-weight(i)) + value(i)    (i번째 물건을 넣음)
둘 중 큰 값.

opt(i-1, ?)는 prev
opt(i, ?)는 cur 배열 사용.
'''
# 처음 입력
n, k = map(int, input().split())

# 배열 초기화
prev = [0 for _ in range(k + 1)]

# 물건 입력
for i in range(n):
	weight, value = map(int, input().split())

	# 가방에 들어가는지 계산
	cur = []
	for j in range(k + 1):
		tmp1 = prev[j]
		tmp2 = prev[j - weight] + value if j - weight >= 0 else 0
		cur.append(max(tmp1, tmp2))
	
	prev = cur

# 출력
print(prev[k])