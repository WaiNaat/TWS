/*
저점: 지워진 번호가 전부 일치하지 않음
고점: 지워진 번호가 전부 일치함
*/

function solution(lottos, win_nums) {
    // 지워진 개수와 맞춘 개수 세기
    let correct = 0;
    let erased = 0;
    
    win_nums = new Set(win_nums);
    
    for (let num of lottos)
    {
        if (num === 0)
            erased++;
        else if (win_nums.has(num))
            correct++;
    }
    
    // 저점과 고점 계산
    const grade = [6, 6, 5, 4, 3, 2, 1];
    return [grade[correct + erased], grade[correct]];
}