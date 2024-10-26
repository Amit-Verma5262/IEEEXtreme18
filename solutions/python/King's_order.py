import heapq
from sys import stdin, stdout

class Project:
    def __init__(self, id, group):
        self.id = id
        self.group = group
    
    def __lt__(self, other):
        if self.group == other.group:
            return self.id < other.id
        return self.group < other.group

n, m = map(int, input().split())
group_id = list(map(int, input().split()))
adj = [[] for _ in range(n)]
in_degree = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    in_degree[b] += 1

pq = []
for i in range(n):
    if in_degree[i] == 0:
        heapq.heappush(pq, Project(i, group_id[i]))

result = []

while pq:
    current = heapq.heappop(pq)
    result.append(current.id + 1)
    
    for neighbor in adj[current.id]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            heapq.heappush(pq, Project(neighbor, group_id[neighbor]))

if len(result) != n:
    print(-1)
else:
    print(" ".join(map(str, result)))
