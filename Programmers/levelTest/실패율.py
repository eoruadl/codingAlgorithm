# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    fail = [0] * (N + 2)
    for i in range(1, N + 2):
        total = 0
        f = 0
        for stage in stages:
            if stage >= i:
                total += 1
            if stage == i:
                f += 1
        if total != 0:
            fail[i] = f / total

    fail.pop(0)
    fail.pop(-1)

    for i in range(len(fail)):
        idx = fail.index(max(fail))
        answer.append(idx + 1)
        fail[idx] = -1
    return answer
