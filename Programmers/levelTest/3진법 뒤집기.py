# 문제 url = "https://school.programmers.co.kr/learn/courses/30/lessons/68935"

def solution(n):
    answer = 0
    three = ""
    while n > 0:
        n, r = divmod(n, 3)
        three = three + str(r)
    revThree = three[::-1]
    for i in range(len(three) - 1, -1, -1):
        answer += 3 ** i * int(revThree[i])

    return answer
