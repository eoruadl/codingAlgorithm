# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = []
        for i in target:
            _min = 100
            for key in keymap:
                if i in key:
                    if _min > key.index(i):
                        _min = key.index(i)
            if _min == 100:
                cnt = []
                answer.append(-1)
                break
            else:
                cnt.append(_min + 1)
        if len(cnt) > 0:
            answer.append(sum(cnt))
    return answer
