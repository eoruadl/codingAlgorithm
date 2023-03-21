# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/138477

def solution(k, score):
    answer = []
    kList = []
    for s in score:
        kList.append(s)
        if len(kList) > k:
            kList.remove(min(kList))
        answer.append(min(kList))
    return answer
