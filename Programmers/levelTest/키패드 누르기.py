# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    keyPad = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
              '4': (1, 0), '5': (1, 1), '6': (1, 2),
              '7': (2, 0), '8': (2, 1), '9': (2, 2),
              '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    lLoc = keyPad['*']
    rLoc = keyPad['#']
    for number in numbers:
        if number in [1, 4, 7]:
            lLoc = keyPad[str(number)]
            answer = answer + "L"
        elif number in [3, 6, 9]:
            rLoc = keyPad[str(number)]
            answer = answer + "R"
        else:
            target = keyPad[str(number)]
            disL = abs(lLoc[0] - target[0]) + abs(lLoc[1] - target[1])
            disR = abs(rLoc[0] - target[0]) + abs(rLoc[1] - target[1])
            if disL < disR:
                lLoc = keyPad[str(number)]
                answer = answer + "L"
            elif disR < disL:
                rLoc = keyPad[str(number)]
                answer = answer + "R"
            elif disR == disL:
                if hand == "left":
                    lLoc = keyPad[str(number)]
                    answer = answer + "L"
                else:
                    rLoc = keyPad[str(number)]
                    answer = answer + "R"
    return answer
