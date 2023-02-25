# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/60061

def possible(answer):
    for x, y, mat in answer:
        if mat == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif mat == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, mat, act = frame  # 기둥 = 0, 보 = 1 / 삭제 = 0, 추가 = 1
        if act == 0:
            answer.remove([x, y, mat])
            if not possible(answer):
                answer.append([x, y, mat])
        if act == 1:
            answer.append([x, y, mat])
            if not possible(answer):
                answer.remove([x, y, mat])
    return sorted(answer)
