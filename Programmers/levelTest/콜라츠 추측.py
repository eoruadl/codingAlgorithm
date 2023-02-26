# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    count = 0
    for i in range(500):
        if num == 1:
            break
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        count += 1

    if num != 1:
        return -1
    return count
