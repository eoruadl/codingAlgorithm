'''
    # 문제
    최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
    정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 
    최빈값이 여러 개면 -1을 return 합니다.

    # 제한사항
        0 < array의 길이 < 100
    -1000 < array의 원소 < 1000

    # 입출력 예
    array	            result
    [1, 2, 3, 3, 3, 4]	3
    [1, 1, 2, 2]	    -1
    [1]	                1
'''

def solution(array):
    dic = {}
    for i in array:
        if dic.get(i) is None:  # 딕셔너리 i 키 값이 없을 때
            dic[i] = 1  # 키 값에 i, value 값에 1 추가
        else:
            dic[i] += 1 # 중복되는 i 키 에 1씩 추가
            
    lots = max(dic.values())    # 최빈값 도출
    lotsDic = {}    # 최빈값 딕셔너리 생성
    
    for key, value in dic.items(): # 딕셔너리 키, 벨류 값 동시에 투입
        if value == lots:   # 벨류 값이 최빈값이면
            lotsDic[key] = value    # key 값에 최빈값 투입
            
    if len(lotsDic.keys()) > 1: # 최빈값이 여러개면
        return -1
    else:
        return list(lotsDic.keys())[0]  # 딕셔너리의 키값들을 리스트로 만들어 준 후 첫번째값 출력