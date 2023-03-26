# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    answer = []
    termDic = {}
    for term in terms:
        termDic[term[0]] = term[2:]
        print(term)

    for i, p in enumerate(privacies):
        y = p[0:4]
        m = p[5:7]
        d = p[8:10]

        new_m = int(m) + int(termDic[p[-1]])
        if new_m > 12:
            if new_m % 12 != 0:
                y = int(y) + new_m // 12
                m = str(new_m % 12).zfill(2)
            else:
                y = int(y) + new_m // 12 - 1
                m = str(12)
        else:
            m = str(new_m).zfill(2)
        
        if int(today[0:4]) > int(y):
            answer.append(i+1)
        if int(today[0:4]) == int(y) and int(today[5:7]) > int(m):
            answer.append(i+1)
        if int(today[0:4]) == int(y) and int(today[5:7]) == int(m) and int(today[8:10]) >= int(d):
            answer.append(i+1)

    return answer