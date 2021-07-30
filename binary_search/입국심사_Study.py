#https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    left = 0
    right = max(times) * n

    while left <= right:
        people = 0
        mid = (left + right)//2

        for t in times:
            people += mid // t

        if people >= n:
            answer = mid
            right = mid-1

        else:
            left = mid +1
    return answer



print(solution(6,[7,10]))
