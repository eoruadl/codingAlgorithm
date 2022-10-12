'''
    # 문제
    첫 번째 분수의 분자와 분모를 뜻하는 denum1, num1, 
    두 번째 분수의 분자와 분모를 뜻하는 denum2, num2가 매개변수로 주어집니다. 
    두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

    # 입출력 예
    denum1  num1    denum2  num2    return
    1       2       3       4       [5, 4]
    9       2       1       3       [29, 6]
    
'''


def solution(denum1, num1, denum2, num2):

    dn3 = (denum1*num2 + denum2*num1)  # 분자값
    n3 = num1 * num2    # 분모값

    num4 = []
    # 분모에 나눠지는 숫자 확인
    for i in range(1, n3+1):
        a = n3/i
        if a.is_integer() == True:  # 정수인지 아닌지 판별
            num4.append(i)

    num5 = []
    # 분모에 나눠지는 숫자가 분자에 나눠지는지 확인
    for j in num4:
        b = dn3/j
        if b.is_integer(): # == Ture 생략가능 
            num5.append(j)

    if len(num5) == 0:  # 나눠지는 값 없으면
        answer = [dn3, n3]
    else:
        answer = [dn3/num5[-1], n3/num5[-1]]

    return answer
