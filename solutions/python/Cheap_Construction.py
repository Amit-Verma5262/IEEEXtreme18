def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def shortest_string(S):
    N = len(S)
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for length in range(1, N + 1):
        for start in range(N - length + 1):
            substring = S[start:start + length]
            parent = list(range(N + 1))
            rank = [0] * (N + 1)

            for i in range(N - length + 1):
                if S[i:i + length] == substring:
                    for j in range(i, i + length - 1):
                        union(parent, rank, j + 1, j + 2)

            connected_components = len(set(find(parent, i) for i in range(1, N + 1)))

            dp[connected_components] = min(dp[connected_components], length)

    result = []
    for k in range(1, N + 1):
        result.append(dp[k] if dp[k] != float('inf') else 0)

    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    S = input().strip()
    result = shortest_string(S)
    print(" ".join(map(str, result)))