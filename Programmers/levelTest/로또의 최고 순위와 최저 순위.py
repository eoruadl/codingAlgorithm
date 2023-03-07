# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    win_rank = {
        "0": 6,
        "1": 6,
        "2": 5,
        "3": 4,
        "4": 3,
        "5": 2,
        "6": 1,
    }
    zero = 0
    win_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        else:
            for num in win_nums:
                if lotto == num:
                    win_cnt += 1
    min_cor = win_cnt
    max_cor = win_cnt + zero
    return [win_rank[str(max_cor)], win_rank[str(min_cor)]]
