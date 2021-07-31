#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    clo_dic = {}
    for cloth in clothes:
        if cloth[1] in clo_dic:
            clo_dic[cloth[1]] +=1
        else:
            clo_dic[cloth[1]] = 1
    cnt = 1
    for i in clo_dic.values():
        cnt *= (i+1)  # 안입은 경우

    return cnt - 1 # 모두 안입은 경우 제거



print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))