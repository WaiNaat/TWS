/*
각 점수를 얻으려면 라이언이 몇 발을 투자해야 하는지 계산
계산의 편의성을 위해 어피치가 맞춘 구역에서 얻는 점수를 2배로 설정

백트래킹으로 가능한 점수조합 전부 확인
만약 화살이 남으면 다 0점에 투자
*/

// global variables
const ryan_info = new Array(11).fill(0);
const visited = new Array(11);
let best_score_info = new Array(11).fill(0);
let best_score_gap = -1;



function solution(n, info) {
    // 어피치 점수 계산
    info.reverse();
    let apeach_score = info.reduce((prev, cur, i) => cur > 0? prev + i : prev, 0);

    // 라이언이 투자해야 하는 화살 수 계산
    info = info.map(x => x + 1);

    // 백트래킹
    ryan_shoot(n,
               info, 
               0, 
               apeach_score,
    );

    if (best_score_gap === -1)
        return [-1];
    else return best_score_info.reverse();
}

function ryan_shoot(arrow, info, ryan_score, apeach_score)
{    
    // recursive step
    let found = false;

    for (let score=0; score<11; score++)
    {
        if (!visited[score] && info[score] <= arrow)
        {
            found = true;

            let get_score = info[score] > 1? score * 2 : score;

            ryan_info[score] = info[score];
            visited[score] = true;

            ryan_shoot(arrow - info[score], info, ryan_score + get_score, apeach_score);

            ryan_info[score] = 0;
            visited[score] = false;
        }
    }

    // base case
    if (found) return;

    ryan_info[0] += arrow;

    let score_gap = ryan_score - apeach_score;

    if (score_gap > 0 && 
        (score_gap > best_score_gap) ||
        (score_gap == best_score_gap && smaller(ryan_info, best_score_info)))
    {
        best_score_info = Array.from(ryan_info);
        best_score_gap = ryan_score - apeach_score;
    }

    ryan_info[0] -= arrow;
}

function smaller(a, b)
{
    for (let i=0; i<11; i++)
    {
        if (a[i] == 0 && b[i] == 0) 
            continue;
        else if (a[i] > 0 && b[i] == 0)
            return true;
        else if (a[i] == 0 && b[i] > 0)
            return false;
        else if (a[i] > b[i])
            return true;
        else if (a[i] < b[i])
            return false;
    }

    return false;
}