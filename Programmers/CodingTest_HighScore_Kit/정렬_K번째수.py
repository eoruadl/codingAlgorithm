'''
    # 문제
    배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
    예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
    array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
    1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
    2에서 나온 배열의 3번째 숫자는 5입니다.
    배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
    commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 
    배열에 담아 return 하도록 solution 함수를 작성해주세요.

    # 입출력 예
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    return = [5, 6, 3]

'''

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# map(함수, 리스트) -> 리스트 값들 하나하나에 함수를 적용시킨다


def solution(array, commands):
    answer = []

    iter_num = len(commands)
    # ex [1, 5, 2, 6, 3, 7, 4]

    for it in range(iter_num):
        i = commands[it][0]-1
        j = commands[it][1]
        k = commands[it][2]-1
    # sorted(array)
    # array.sort()

        pre_sorted = array[i:j]
        answer.append(sorted(pre_sorted)[k])
    # pre_sorted.sort() -> 원본(변수)을 건드림
    # sorted(pre_sorted) -> 원본(변수)을 건드림 X

    return answer


'''
    def solution(array, commands):
        answer = []
        
        for i in range(len(commands)):
            a = array[commands[i][0]-1:commands[i][1]]

            b = sorted(a)

            answer.append(b[commands[i][2]-1])
        return answer
'''
