/*
백트래킹
현재 보드, A위치, B위치, 움직임 횟수, 차례를 입력받아서 움직여봄
리턴값: 현재 차례인 사람이 이기면 (true, 턴수) 지면 (false, 턴수)

이기는 경우가 하나라도 있다면 그 중 가장 빨리 이기는 거 선택
지는 경우가 하나라도 있다면 그 중 가장 늦게 지는 거 선택
*/

const directions = [[-1, 0], [1, 0], [0, 1], [0, -1]];
let row, col;

function solution(board, aloc, bloc) {
    row = board.length;
    col = board[0].length;
    
    let [result, answer] = play(0, board, ...aloc, ...bloc);
    
    return answer;
}

function play(moves, board, player_r, player_c, opponent_r, opponent_c)
{   
    // base case
    // 패배 조건: 움직일 수 없음
    if (!can_move(board, player_r, player_c))
    {
        return [false, moves];
    }
    
    // 승리 조건: 본인이 움직일 수 있는데 본인과 상대가 같은 칸임
    if (player_r == opponent_r && player_c == opponent_c)
        return [true, moves + 1];
    
    // recursive step
    let can_win = false;
    let min_moves = Infinity;
    let max_moves = -Infinity;
    
    // 상하좌우 경우의 수 확인
    for (let [dr, dc] of directions)
    {
        let r2 = player_r + dr;
        let c2 = player_c + dc;
        
        if (out_of_bounds(r2, c2) || board[r2][c2] == 0)
            continue;
        
        board[player_r][player_c] = 0;
        let [result, result_moves] = play(moves + 1, board, opponent_r, opponent_c, r2, c2);
        board[player_r][player_c] = 1;
        
        if (result) // 상대편이 이겼다면 나는 진거임
            max_moves = Math.max(result_moves, max_moves);
        else // 상대편이 졌다면 나는 이긴거임
        {
            can_win = true;
            min_moves = Math.min(result_moves, min_moves);
        }
    }
    
    return can_win? [true, min_moves] : [false, max_moves];    
}

function can_move(board, r, c)
{
    for (let [dr, dc] of directions)
    {
        let r2 = r + dr;
        let c2 = c + dc;
        
        if (!out_of_bounds(r2, c2) && board[r2][c2] == 1)
            return true;
    }
    return false;
}

function out_of_bounds(r, c)
{
    if (0 > r || r >= row || 0 > c || c >= col) return true;
    else return false;
}