# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    cal = [[0], [0] * 32, [0] * 30, [0] * 32, [0] * 31, [0] * 32, [0] * 31, [0] * 32, [0] * 32,
           [0] * 31, [0] * 32, [0] * 31, [0] * 32]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    monLen = len(cal)
    idx = 0
    for i in range(1, monLen):
        for j in range(1, len(cal[i])):
            cal[i][j] = days[idx % 7]
            idx += 1
    return cal[a][b]


def getDayName(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1) % 7]
