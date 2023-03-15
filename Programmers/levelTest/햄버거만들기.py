# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    a = []
    for i in ingredient:
        a.append(i)
        if a[-4:] == [1, 2, 3, 1]:
            del a[-4:]
            answer += 1

    return answer
