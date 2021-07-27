#https://www.acmicpc.net/problem/15903
import sys
import heapq

n,m = map(int, sys.stdin.readline().split())
card = list(map(int,sys.stdin.readline().split()))

heapq.heapify(card)
stack=[]

for i in range(m):
    stack.append(heapq.heappop(card))
    stack.append(heapq.heappop(card))
    heapq.heappush(card,stack[-1]+stack[-2])
    heapq.heappush(card,stack[-1] + stack[-2])

print(sum(card))
