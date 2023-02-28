# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    result = [0] * 4
    idx = 0
    num = 0
    for i in dartResult:
        if i.isdigit():
            if num == 0:
                num = i
                idx += 1
                result[idx] = num
            else:
                num = num + i
                result[idx] = num

        if not i.isdigit():
            num = 0
            if i == "S":
                result[idx] = int(result[idx]) ** 1
            elif i == "D":
                result[idx] = int(result[idx]) ** 2
            elif i == "T":
                result[idx] = int(result[idx]) ** 3

            if i == "*":
                result[idx] = result[idx] * 2
                result[idx-1] = result[idx-1] * 2
            elif i == "#":
                result[idx] = int(result[idx] * -1)
    return sum(result)
