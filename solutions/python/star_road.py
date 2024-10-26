from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(100000)

def dfs(city, last_star):
    if dp[city] != -1:
        return dp[city]
    
    max_restaurants = 1
    for neighbor in adj[city]:
        if stars[neighbor] > last_star:
            max_restaurants = max(max_restaurants, 1 + dfs(neighbor, stars[neighbor]))
    
    dp[city] = max_restaurants
    return dp[city]

# Input
N = int(input())
adj = [[] for _ in range(N + 1)]
stars = [0] * (N + 1)
dp = [-1] * (N + 1)

# Read stars array
stars = [0] + list(map(int, input().split()))

# Read edges
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# Calculate maximum path
max_path = 0
for i in range(1, N + 1):
    max_path = max(max_path, dfs(i, -1))

print(max_path)
