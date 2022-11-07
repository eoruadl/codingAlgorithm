# 문제 url : https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    # 0 부터 9까지 딕셔너리 만들어주기
    dic = {}
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        dic[en[i]] = i
    
    # 결과를 담을 변수
    result = ""
    # 영문자를 담을 변수
    re = ""
    for i in s:
        # 숫자면 결과에 담기
        if i.isdigit():
            result += i
        # 영문자면 re에 담기
        elif i.isalpha():
            re += i
            # 만약 영문자가 담긴 re 가 dic에 있으면
            if re in dic:
                # 결과에 키값을 문자열로 바꿔 담기
                result += str(dic[re])
                # re 값 초기화
                re = ""
    answer = int(result)
    return answer

def solution2(s):
    answer = s
    dic = {}
    en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        dic[en[i]] = str(i)
    
    for key, value in dic.items():
        answer = answer.replace(key, value)
    return int(answer)