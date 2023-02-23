# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    s_split = s.split(" ")
    answer = []
    for i in s_split:
        s_list = list(i)
        for j in range(len(s_list)):
            if j % 2 == 0:
                s_list[j] = s_list[j].upper()
            else:
                s_list[j] = s_list[j].lower()
        answer.append(''.join(s_list))
    return " ".join(answer)
