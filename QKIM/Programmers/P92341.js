/*
A가 B를 여러 번 신고할 수 있지만 1회로 처리
    >> 각 사람별로 누구를 신고했는지 Set에 저장해서 중복 검사

결과 메일은 '신고한' 사람에게 통보

사람별로 누구에게 신고당했는지 저장하는 set들의 Map(key: 사람이름, value:Set)
여기에 신고들을 처리해서 판별 가능

결과는 배열 >> 사람이름-배열 idx 연결해주는 Map
*/

function solution(id_list, report, k) {
    const reported_list = new Map();
    const id_map = new Map();

    // 두 Map 초기화
    for (let i=0; i<id_list.length; i++)
    {
        id_map.set(id_list[i], i);
        reported_list.set(id_list[i], new Set());
    }

    // 신고 처리
    for (let r of report)
    {
        let [from, to] = r.split(' ');
        reported_list.get(to).add(from);
    }

    // 결과 메일 말송
    const answer = new Array(id_list.length).fill(0);

    for (let id of id_list)
    {
        let reported = reported_list.get(id);

        if (reported.size >= k)
        {
            for (let mail_to of reported)
                answer[id_map.get(mail_to)]++;
        }
    }

    return answer;
}