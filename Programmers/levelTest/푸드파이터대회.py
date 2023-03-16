# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    arr = ''
    for i in range(1, len(food)):
        if food[i] // 2 > 0:
            arr += str(i) * (food[i] // 2)
    answer = arr + "0" + arr[::-1]
    return answer
