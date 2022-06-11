"""
function DividePaper
	BASE CASE: 
		input이 하얀색으로만, 또는 파란색으로만 구성되어 있는지 확인
		만약 그렇다면 count 증가시킴
	RECURSIVE STEP:
		input의 색이 섞여 있으면 4등분해서 재귀
"""
#init
whitePaper = 0
bluePaper = 0
paper = []

#input
N = int(input())
for i in range(N):
	paper.append(list(map(int, input().split())))

#alg
def DividePaper(startX, startY, length):
	global whitePaper
	global bluePaper
	colors = 0

	for i in range(length):
		colors += sum(paper[startY + i][startX : startX + length])

	if colors == 0:
		whitePaper += 1
		return
	elif colors == length*length:
		bluePaper += 1
		return
	
	length = int(length/2)
	DividePaper(startX, startY, length)
	DividePaper(startX, startY + length, length)
	DividePaper(startX + length, startY, length)
	DividePaper(startX + length, startY + length, length)
	return

DividePaper(0, 0, N)

#output
print(whitePaper)
print(bluePaper)

'''
arr = []

arr.append(list(map(int, input().split())))
arr.append(list(map(int, input().split())))

print(arr)
'''