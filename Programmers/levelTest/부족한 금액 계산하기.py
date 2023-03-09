# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    price_cnt = price
    total = 0
    for i in range(count):
        total += price_cnt
        price_cnt += price
    if money >= total:
        return 0
    else:
        return total - money
