# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        divs = []
        for j in range(1, i + 1):
            if i % j == 0:
                divs.append(j)

        if len(divs) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
