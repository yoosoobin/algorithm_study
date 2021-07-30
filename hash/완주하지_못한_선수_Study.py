#https://programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter

def solution(participant, completion):
    p=Counter(participant)
    c=Counter(completion)
    f=list(p-c)
    for i in f:
        return i

fail = solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])
print(fail)