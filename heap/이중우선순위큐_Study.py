#https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq


def solution(operations):
    answer = []

    for i in operations:
        if i[0] == 'I':
            heapq.heappush(answer,int(i[2:]))
        elif i[0] == 'D':
            if len(answer) == 0:
                pass
            elif int(i[2:]) == -1:
                heapq.heappop(answer)
            else:
                answer.sort()
                answer.pop()

    if len(answer) == 0:
        return [0,0]
    else:
        return [max(answer),answer[0]] # heap은 가장 우선순위가 높은 값이 먼저 pop되는 것을 보장하는 자료구조
                                      # answer[0]이 가장 작은값인것은 맞으나, 나머지 값에 대한 정렬은 보장하지 않는다!!


print(solution(["I 16","I 26","I 36","I 46","D -1","D 1"]))



