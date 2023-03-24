# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    _s = ''
    for i in s:
        if i not in _s:
            answer.append(-1)
            _s += i
        elif i in _s:
            idx = _s.rindex(i)
            l = len(_s) - idx
            _s += i
            answer.append(l)
    return answer
