/*
트리 탐색
enroll과 referral로 parent를 Map obj로 만들어서 찾기 쉽게 한다.
돈 분배는 재귀를 이용해서 트리를 탐색하면 구현 가능
분배된 돈 역시 Map obj에 저장한다.
*/

const parent = new Map();
const income = new Map();

function solution(enroll, referral, seller, amount) {
    // map obj 초기화
    for (let i=0; i<enroll.length; i++)
    {
        parent.set(enroll[i], referral[i]);
        income.set(enroll[i], 0);
    }
    
    // 이익 분배
    for (let i=0; i<seller.length; i++)
        distribute_money(seller[i], amount[i] * 100);
    
    // 정답 만들기
    let answer = [];
    for (let name of enroll)
        answer.push(income.get(name));
    
    return answer;
}

function distribute_money(name, money)
{
    // base case
    if (name === '-')
        return;
    
    // recursive step
    let give = Math.floor(money / 10);
    
    income.set(name, income.get(name) + money - give);
    if (give > 0)
        distribute_money(parent.get(name), give);
}