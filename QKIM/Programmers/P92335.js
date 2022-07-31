function solution(n, k) {
    const numbers = n.toString(k).split(/0+/);
    
    let cnt = 0;
    for (let num of numbers)
        cnt += isPrime(num);

    return cnt;
}

function isPrime(val)
{
    if (val < 2) return 0;

    for (let i=2; i**2<=val; i++)
        if (val % i === 0) return 0;

    return 1;
}