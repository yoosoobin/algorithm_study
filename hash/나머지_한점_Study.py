#https://programmers.co.kr/learn/courses/18/lessons/1878?language=python3

from collections import Counter



def solution(arr):
    x = []
    y = []

    for dot in arr:
        x.append(int(dot[0]))
        y.append(int(dot[1]))

    x = Counter(x)
    y = Counter(y)

    ans_x = x.most_common(2)[1][0]
    ans_y = y.most_common(2)[1][0]
    return [ans_x, ans_y]


ans = solution([[1, 1], [2, 2], [1, 2]])
print(ans)


