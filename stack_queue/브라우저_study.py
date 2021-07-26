#http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=294&sca=99&sfl=wr_homepage&stx=East+Central+North+A
from collections import deque
import sys

f_stack = deque()
b_stack = deque()

adr = 'http://www.acm.org/'
b_stack.append(adr)

def back():
    if len(b_stack) != 1:
        f_stack.append(b_stack.pop())
        print(b_stack[-1])
    else:
        print('Ignored')

def forward():
    if len(f_stack) != 0:
        b_stack.append(f_stack.pop())
        print(b_stack[-1])
    else:
        print('Ignored')

def visit(adress):
    b_stack.append(adress)
    f_stack.clear()
    print(b_stack[-1])

x=True

while x:
    c = list(sys.stdin.readline().split())
    if c[0] == 'VISIT':
        visit(c[1])
    elif c[0] == 'QUIT':
        break
    elif c[0] == 'BACK':
        back()
    elif c[0] == 'FORWARD':
        forward()



