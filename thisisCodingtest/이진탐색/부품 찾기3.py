# 집합 자료형 이용한 풀이
# 집합 자료형은 단순히 특정한 데이터가 존재하는지 검사할 때에 매우 효과적으로 사용


n = int(input())
# 가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end=" ")
    else:
        print('no', end=" ")
