'''
    # 문제
    수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
    마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
    완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

    # 제한사항
    마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
    completion의 길이는 participant의 길이보다 1 작습니다.
    참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
    참가자 중에는 동명이인이 있을 수 있습니다.

    # 입출력 예
    participant	                                        completion	                                return
    ["leo", "kiki", "eden"]	                            ["eden", "kiki"]	                        "leo"
    ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
    ["mislav", "stanko", "mislav", "ana"]	            ["stanko", "ana", "mislav"]	                "mislav"

'''

# 해쉬 클래스를 이용한 코드
def solution1(participant, completion):
    answer = ''
    hDic = {} # 해쉬 딕셔너리를 만든다
    sumH = 0
    
    for part in participant:
        hDic[hash(part)] = part # hash 클래스로 key 값을 hash 값으로 바꿔줌
        sumH += hash(part)      # hash 값을 더해준다

    for comp in completion:
        sumH -= hash(comp)      # 완주자들의 hash 값을 빼준다.
    
    answer = hDic[sumH]         # 남은 해쉬값의 key 가 미완주자이다.
    
    return answer

# counter 클래스를 이용한 코드 (collections 모듈 필요)
import collections

def solution2(participant, completion):
    # Counter 클래스는 리스트를 딕셔너리로 바꿔주며 value에 key를 카운트한 값을 넣어준다.
    answer = collections.Counter(participant) - collections.Counter(completion)
    # 두 값을 빼주면 미완주자만 key 값으로 남게된다.
    
    # 딕셔너리의 key 값을 리스트로 만들어주고 출력해준다.
    return list(answer.keys())[0]


# 내가 풀이한 코드 (시간초과로 실패 / 정확성은 성공)
def solution3(participant, completion):
    answer = ''
    a = participant
    b = completion
    
    dicA = {}
    dicB = {}
    
    for i in a:
        if dicA.get(i) is None:
            dicA[i] = 1
        else:
            dicA[i] += 1
    
    for j in b:
        if dicB.get(j) is None:
            dicB[j] = 1
        else:
            dicB[j] += 1
    
    for key, value in dicA.items():
        for c, d in dicB.items():
            if c != key:
                pass
            elif c == key:
                if d != value:
                    answer = c
                else: pass
        if key not in dicB:
            answer = key
            
    return answer
