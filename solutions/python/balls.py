data = [int(x) for x in input().split()]
n = data[0]
k = data[1]

e_balls = [int(x) for x in input().split()]

count = 0

def count_multiples(a, b):
    product = a * b
    if product == 0:
        return 0  
    return n // product


for e in e_balls:

    e_balls_copy = e_balls.copy()

    count += n // e
    
    limit = e_balls_copy[e_balls_copy.index(e)+1:]

    for p in limit:
        count -= count_multiples(e, p)


print(count)


