# 문제 url : https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d:
        if i <= budget:
            budget = budget - i
            answer += 1
    return answer