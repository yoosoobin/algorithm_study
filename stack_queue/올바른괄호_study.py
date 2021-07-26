#https://programmers.co.kr/learn/courses/30/lessons/12909

import sys
from collections import deque

s = sys.stdin.readline().strip()
stack = deque()

def solution(s):
    for i in range(len(s)):
        stack.append(s[i])
        if len(stack) >= 2:
            if stack[-2] == '(' and stack[-1] == ')':
                stack.pop()
                stack.pop()
            else:
                pass
        else:
            pass

    if len(stack) == 0:
        print('true')
    else:
        print('false')


solution(s)


