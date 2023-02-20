# 문제 url : https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    # 차집합으로 여분을 가지고 있지만 도난당한 학생을 걸러냄
    reserve_student = set(reserve) - set(lost)
    lost_student = set(lost) - set(reserve)

    for student in reserve_student:
        if (student - 1) in lost_student:
            lost_student.remove(student - 1)
        elif (student + 1) in lost_student:
            lost_student.remove(student + 1)

    return n - len(lost_student)
