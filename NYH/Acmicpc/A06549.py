import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(array):
    result = []
    for arr in array:
        result.append(sub_ploblem(arr[0], arr[1:]))
    return result

def sub_ploblem(n, heights):
    return div(0, n - 1, heights)

def div(left, right, heights):
    if left == right: 
        return heights[left]

    mid = (left + right) // 2

    left_area = div(left, mid, heights)
    right_area = div(mid + 1, right, heights)

    left_pointer = mid
    right_pointer = mid
    mid_area = heights[mid]
    min_height = heights[mid]
    
    while(left <= left_pointer and right_pointer <= right):
        min_height = min(heights[right_pointer], heights[left_pointer], min_height)
        mid_area = max(mid_area, (right_pointer - left_pointer + 1) * min_height)

        if left_pointer == left:
            right_pointer += 1
        elif right_pointer == right:
            left_pointer -= 1
        elif heights[left_pointer - 1] <= heights[right_pointer + 1]:
            right_pointer += 1
        else:
            left_pointer -= 1


    return max(mid_area, left_area, right_area)

if __name__=="__main__":
    array = []
    while True:
        arr = list(map(int,input().split()))
        if arr[0] == 0:
            break
        array.append(arr)

    for sol in solution(array):
        print(sol)