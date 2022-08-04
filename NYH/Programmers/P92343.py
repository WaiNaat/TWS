
def solution(info, edges):
    
    n = len(info)

    visited = [False] * n
    visited[0] = True
    answer = []

    def dfs(s, w):
        if s > w:
            answer.append(s)
        else:
            return
        for i in range(n - 1):
            parent = edges[i][0]
            child = edges[i][1]
            isWolf = info[child]

            if visited[parent] and not visited[child]:
                visited[child] = True
                dfs(s + (isWolf == 0), w + (isWolf == 1))
                visited[child] = 0

    dfs(1, 0)

    return max(answer)



info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [
    [0,1],[1,2],[1,4],
    [0,8],[8,7],[9,10],
    [9,11],[4,3],[6,5],
    [4,6],[8,9]
]


print(solution(info, edges))