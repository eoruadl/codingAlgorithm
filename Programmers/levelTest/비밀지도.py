# 문제 url = "https://school.programmers.co.kr/learn/courses/30/lessons/17681"

def solution1(n, arr1, arr2):
    answer = []
    list1=[]
    # 두 개의 리스트 값을 a, b로 넣어준다
    for a, b in zip(arr1, arr2):
        # list1 에 a, b를 비트연산 or 로 해주어 인덱스 2부터 넣어준다.
        list1.append(bin(a | b)[2:].zfill(n))
        # zfill 함수는 n 숫자자리수를 만족 못하면 앞에서 부터 0 으로 채워준다.

    for i in list1:
        tmp = i.replace('1', '#').replace('0', ' ') # 1은 #으로 0은 ' ' 로 바꿔준다.
        answer.append(tmp)
    return answer

def solution2(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = bin(arr1[i] | arr2[i])[2:].zfill(n)
        tmp = tmp.replace('1', '#').replace('0', ' ')
        answer.append(tmp)
    return answer

def solution3(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        # rjust 함수는 n자리수로 만들어주며 빈자리를 0으로 채워주는 함수
        # r = 오른쪽 정렬
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer