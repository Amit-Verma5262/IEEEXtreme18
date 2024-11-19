N = int(input())

r = range(1, 2*N+1)

A, B = 0, 1

blocks = dict()

for e in map(int, input().split()):
    blocks[e] = A

for e in map(int, input().split()):
    blocks[e] = B
