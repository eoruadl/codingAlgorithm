# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    person = {"수포자 1": [1, 2, 3, 4, 5],
              "수포자 2": [2, 1, 2, 3, 2, 4, 2, 5],
              "수포자 3": [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]}
    aCount = []

    for aList in person.values():
        count = 0
        for i in range(len(answers)):
            if answers[i] == aList[i % len(aList)]:
                count += 1
        aCount.append(count)

    maxA = 0
    for idx, i in enumerate(aCount):
        if i > maxA:
            answer = []
            maxA = i
            answer.append(idx + 1)
        elif i == maxA:
            answer.append(idx + 1)
    return answer
