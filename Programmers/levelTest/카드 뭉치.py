# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    for g in goal:
        if g == cards1[0]:
            a = cards1.pop(0)
            cards1.append(a)
        elif g == cards2[0]:
            a = cards2.pop(0)
            cards2.append(a)
        else:
            return "No"
    return "Yes"
