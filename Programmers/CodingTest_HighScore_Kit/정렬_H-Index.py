'''
    # 문제
    H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 
    어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 
    위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

    어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 
    나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

    어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 
    이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

    # 입출력 예
    citations = [3, 0, 6, 1, 5]
    return = 3
'''

def solution(citations):
    # 오름차순으로 정렬
    a = sorted(citations)
    
    # 최대 길이 만큼 반복
    for i in range(len(a)):
        # h번 이상 인용된 논문이 h편 이상 이라는 문장을 코드로 표현
        # 총 논문수 에서 인덱스 값만큼 빼주면 h 편 이상을 나타낼 수 있음
        if a[i] >= len(a)-i:
            return len(a)-i
    return 0