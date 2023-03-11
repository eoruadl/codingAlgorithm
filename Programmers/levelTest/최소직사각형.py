# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    w = 0
    h = 0
    if sizes[0][0] > sizes[0][1]:
        w = sizes[0][0]
        h = sizes[0][1]
    else:
        w = sizes[0][1]
        h = sizes[0][0]

    for size in sizes:
        if size[0] > size[1]:
            if size[0] > w:
                w = size[0]
            if size[1] > h:
                h = size[1]
        else:
            if size[1] > w:
                w = size[1]
            if size[0] > h:
                h = size[0]
    return w * h
