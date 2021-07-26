#https://www.acmicpc.net/problem/10845
from collections import deque
import sys

que = deque()

def push(x):
    que.append(int(x))

def pop():
    if len(que) != 0:
        print(que.popleft())
    else:
        print(-1)

def size():
    print(len(que))

def empty():
    if len(que) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(que) != 0:
        print(que[0])
    else:
        print(-1)

def back():
    if len(que) != 0:
        print(que[-1])
    else:
        print(-1)

def main():
    n = int(sys.stdin.readline().strip())

    for i in range(n):
        c = list(sys.stdin.readline().split())
        if c[0]=='push':
            push(c[1])
        elif c[0] == 'pop':
            pop()
        elif c[0] == 'size':
            size()
        elif c[0] == 'empty':
            empty()
        elif c[0] == 'front':
            front()
        elif c[0] == 'back':
            back()

main()

