# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()

    # 2
    for i in new_id:
        if i.isalpha() or i.isdigit() or i in ['-', '_', '.']:
            answer += i

    # 3
    while ".." in answer:
        answer = answer.replace("..", ".")

    # 4
    answer = answer.strip(".")

    # 5
    if answer == "":
        answer += "a"

    # 6
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip(".")

    # 7
    while len(answer) < 3:
        answer += answer[-1]

    return answer
