# 문제 url : https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    pDic = {}
    for num in nums:
        if pDic.get(num) is None:
            pDic[num] = 1
        else:
            pDic[num] += 1
            
    a = len(pDic)
    b = len(nums)
    if b / 2 <= a:
        answer = b / 2
    else:
        answer = a
    
    return answer