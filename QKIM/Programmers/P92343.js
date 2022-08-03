/*
edges 정리해서 인접 배열 형태로 만들기

탐색 방법
방문 가능한 노드 배열을 만든다
그 배열을 순회하면서 해당 위치로 진짜 이동이 가능한지 확인하고
이동이 가능하면 그 위치로 이동하고 거기랑 인접한 노드를 다시 배열에 넣음

진짜 이동이 가능한지 확인하는 것?
해당 노드에 대해 백트래킹으로 어디까지 갈 수 있는지 확인
만약 끝까지 갔는데 양이 없었다면 데려갔던 늑대들 다시 제거
*/

let sheep = 0;
let wolf = 0;
let E;
let found;
let visited;

function solution(info, edges) {    
    // edges 정리
    E = Array.from(new Array(info.length), () => []);
    for (let [u, v] of edges)
    {
        E[u].push(v);
        E[v].push(u);
    }
    
    // 탐색
    let adj = Array.from(E[0]);
    found = true;
    visited = new Array(info.length);
    
    while (found)
    {
        found = false;
        let adj2 = [];
        
        for (let next of adj)
        {
            if (visited[next]) continue;
            search(next, visited, adj2, info);
        }
        
        console.log(sheep, wolf);
        console.log(adj2);
                    
        adj = adj2;
    }
    
    return sheep;
}

function search(node, visited, adj2, info)
{
    let sheep_found = false;
    
    for (let child of E[node])
    {
        if (visited[child]) continue;
        visited[child] = true;
        
        // 양
        if (info[child] == 0)
        {
            sheep++;
            found = true;
            console.log(child, sheep, wolf);
            search(child, visited, adj2, info);
            adj2.push(...E[child]);
            sheep_found = sheep_found || true;
        }
        // 늑대인데 데려가면 안되는 늑대
        else if (wolf + 1 >= sheep)
        {
            adj2.push(child);
            visited[child] = false;
            sheep_found = sheep_found || false;
        }
        // 데려갈 수 있는 늑대
        else
        {
            wolf++;
            
            if (search(child, visited, adj2, info)) // 해당 늑대부터 출발해서 양을 데려갈 수 있으면 ok
                sheep_found = sheep_found || true;
            else
            {
                wolf--;
                visited[child] = false;
                sheep_found = sheep_found || false;
            }
        }
    }
    
    return sheep_found;
}