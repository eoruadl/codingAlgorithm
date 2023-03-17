# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    s_score = sorted(score, reverse=True)
    box = []
    for a in s_score:
        box.append(a)
        if len(box) == m:
            answer += box[-1] * m
            box = []
    return answer
