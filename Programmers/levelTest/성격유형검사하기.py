# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    ind = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    point = [0, 3, 2, 1, 0, 1, 2, 3]

    for i in range(len(survey)):
        if choices[i] <= 3:
            ind[survey[i][0]] += point[choices[i]]
        else:
            ind[survey[i][1]] += point[choices[i]]

    if ind["R"] >= ind["T"]:
        answer += 'R'
    else:
        answer += 'T'
    if ind["C"] >= ind["F"]:
        answer += 'C'
    else:
        answer += 'F'
    if ind["J"] >= ind["M"]:
        answer += 'J'
    else:
        answer += 'M'
    if ind["A"] >= ind["N"]:
        answer += 'A'
    else:
        answer += 'N'
    return answer
