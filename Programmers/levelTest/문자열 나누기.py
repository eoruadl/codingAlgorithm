# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    sList = []
    _s = ''
    f = ''
    for i in range(len(s)):
        _s += s[i]
        if len(_s) == 1:
            f = _s
        cnt = _s.count(f)
        if cnt == len(_s) - cnt:
            sList.append(_s)
            f = ''
            _s = ''
        if i == len(s) - 1:
            if _s != '':
                sList.append(_s)
    return len(sList)
