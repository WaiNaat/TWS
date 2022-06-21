import sys

def input():
    return sys.stdin.readline().rstrip()

def solution(L, C, words):
    '''
        a, e, i, o, u중 최소 한개가 포함
        나머지 자음 중 최소 두개가 포함
        L : 길이
    '''
    words.sort()
    sub_ploblem([], L, C, words, 0)

def sub_ploblem(word, L, C, words, idx):
    
    # 종료 조건
    if len(word) == L:
        vowels = len_vowels(word)
        if vowels >= 1 and len(word) - vowels >= 2:
            print("".join(map(str, word)))
        return
    
    for i in range(idx, C):
        word.append(words[i])
        sub_ploblem(word, L, C, words, i + 1)
        word.pop()


def len_vowels(word):
    check_set = set(["a","e","i","o","u"])
    word_set = set(word)
    return len(list(check_set & word_set))


if __name__=="__main__":
    L, C = map(int,input().split())
    words = list(input().split())
    solution(L, C, words)