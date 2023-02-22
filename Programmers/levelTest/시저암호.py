# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr(ord("A") + ((ord(s[i]) - ord("A") + n) % 26))
        elif s[i].islower():
            s[i] = chr(ord("a") + ((ord(s[i]) - ord("a") + n) % 26))
    return "".join(s)
