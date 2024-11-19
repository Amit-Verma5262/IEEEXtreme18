N, Q = map(int, input().split())

A = [0] * (N+1)
P = [0]+ list(map(int, input().split()))


for _ in range(Q):
    Ti, *args = map(int, input().split())

    if (Ti == 0):
        l, r, c = args
        for i in range(l, r+1):
            A[i] += c  
    elif (Ti == 1):
        l, r, c = args
        for i in range(l, r+1):
            A[P[i]] += c
    elif (Ti == 2):
        l, r = args
        print(sum(A[l:r+1]))
    
    else:
        l, r = args
        print(sum(map(lambda x:A[P[x]], range(l, r+1))))
    