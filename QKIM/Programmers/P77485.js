function solution(rows, columns, queries) {
    // 초기 행렬 만들기
    let matrix = Array.from(new Array(rows), () => new Array(columns));
    let num = 1;
    
    for (let r=0; r<rows; r++)
    {
        for (let c=0; c<columns; c++)
            matrix[r][c] = num++;
    }
    
    // 쿼리 수행
    let answer = [];
    
    for (let [r1, c1, r2, c2] of queries)
        answer.push(rotate(matrix, r1 - 1, c1 - 1, r2 - 1, c2 - 1));
    
    return answer;
}

function rotate(matrix, r1, c1, r2, c2)
{
    let min = matrix[r1][c1];
    let val = matrix[r1][c1];
    
    // 좌
    for (let r=r1; r<r2; r++)
    {
        matrix[r][c1] = matrix[r + 1][c1];
        min = Math.min(min, matrix[r][c1]);
    }
    // 하
    for (let c=c1; c<c2; c++)
    {
        matrix[r2][c] = matrix[r2][c + 1];
        min = Math.min(min, matrix[r2][c]);
    }
    // 우
    for (let r=r2; r>r1; r--)
    {
        matrix[r][c2] = matrix[r - 1][c2];
        min = Math.min(min, matrix[r][c2]);
    }
    // 상
    for (let c=c2; c>c1; c--)
    {
        matrix[r1][c] = matrix[r1][c - 1];
        min = Math.min(min, matrix[r1][c]);
    }
    matrix[r1][c1 + 1] = val;
    
    return min;
}