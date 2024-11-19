import math

data = [int(x) for x in input().split()]
N = data[0]
M = data[1]


x = int((N-1)/2)


swaps = 0

swaps = 2 * sum(i for i in range(0, x+1)) * math.factorial(N - 1)

swaps = swaps + 2 * sum((sum(i for i in range(0, x-p+1))) for p in range(1, x+1))

print(swaps % M)