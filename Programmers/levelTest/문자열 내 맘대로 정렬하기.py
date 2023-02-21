# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    strList = []
    for string in strings:
        a = string[n] + string
        strList.append(a)
    strList.sort()

    for i in strList:
        answer.append(i[1:])
    return answer


# sorted 함수의 key 매개변수 활용
def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))  # 튜플로 우선순위 지정 가능
