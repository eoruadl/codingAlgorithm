'''
    # 문제
    두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

    # 입력
    입력은 여러 개의 테스트 케이스로 이루어져 있다.
    각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

    # 출력
    각 테스트 케이스마다 A+B를 출력한다.
'''

while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break

# 1(True) 로 적용한 while문을 이용하여 try와 except를 이용해 try의 조건을 만족하지 못할 경우 except로 처리하여 break 시킨다.