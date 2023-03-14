# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    pronoun = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for pro in pronoun:
            if pro * 2 not in bab:
                bab = bab.replace(pro, " ")
        if bab.strip() == "":
            answer += 1
    return answer
