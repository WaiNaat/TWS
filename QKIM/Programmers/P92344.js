/// 누적합 공부하기 ///

function solution(board, skill) {
    // 각 스킬의 영향 범위를 표시
    const row = board.length;
    const col = board[0].length;
    const prefix_sum = Array.from(new Array(row + 1), () => new Array(col + 1).fill(0));
    
    for (let [type, r1, c1, r2, c2, degree] of skill)
    {        
        let flag;
        if (type === 1) flag = 1;
        else flag = -1;
        
        prefix_sum[r1][c1] += flag * degree;
        prefix_sum[r1][c2 + 1] += -flag * degree;
        prefix_sum[r2 + 1][c1] += -flag * degree;
        prefix_sum[r2 + 1][c2 + 1] += flag * degree;        
    }
    
    // 누적합 계산
    for (let r=0; r<row; r++)
    {
        for (let c=1; c<col; c++)
            prefix_sum[r][c] += prefix_sum[r][c - 1];
    }
    
    for (let c=0; c<col; c++)
    {
        for (let r=1; r<row; r++)
            prefix_sum[r][c] += prefix_sum[r - 1][c];
    }
    
    // 정답 계산
    let cnt = 0;
    for (let r=0; r<row; r++)
    {
        for (let c=0; c<col; c++)
        {
            if (board[r][c] > prefix_sum[r][c])
                cnt++;
        }
    }
    
    return cnt;
}