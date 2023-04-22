# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/161989

from collections import deque


def solution(n, m, section):
    answer = 0
    section = deque(section)

    while section:
        start = section.popleft()

        while section and start + m > section[0]:
            section.popleft()
        answer += 1

    return answer
