# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    answer = [True] * (n + 1)
    for i in range(2, n + 1):
        if answer[i]:
            for j in range(i*2, n + 1, i):
                answer[j] = False
    return len([i for i in range(2, n + 1) if answer[i]])
