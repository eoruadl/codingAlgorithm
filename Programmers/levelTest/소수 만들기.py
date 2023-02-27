# 문제 url = https://school.programmers.co.kr/learn/courses/30/lessons/12977

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                if is_prime(num):
                    answer += 1
    return answer
