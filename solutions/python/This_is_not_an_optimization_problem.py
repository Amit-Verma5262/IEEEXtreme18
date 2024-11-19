from collections import defaultdict
import heapq
from itertools import combinations

N = int(input())
W = list(map(int, input().split()))

AM = defaultdict(list)


for _ in range(N-1):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    # AM[i][j] = 1
    # AM[j][i] = 1
    AM[i].append(j)
    AM[j].append(i)


def calculate_all_pairs_cost(N, graph_weights, adjacency_list):
    # Create a matrix to store the shortest path costs between nodes
    cost_matrix = [[float('inf')] * N for _ in range(N)]
    
    # Function to run modified Dijkstra's algorithm from a given start node
    def dijkstra(start):
        min_heap = [(graph_weights[start], start)]  # (current cost, node)
        cost_matrix[start][start] = graph_weights[start]
        
        while min_heap:
            current_cost, node = heapq.heappop(min_heap)
            
            # Check each neighbor
            for neighbor in adjacency_list[node]:
                new_cost = current_cost + graph_weights[neighbor]
                
                # If the new cost is lower, update and push to heap
                if new_cost < cost_matrix[start][neighbor]:
                    cost_matrix[start][neighbor] = new_cost
                    heapq.heappush(min_heap, (new_cost, neighbor))
                    
    # Run Dijkstra's from each node
    for start in range(N):
        dijkstra(start)
    
    return cost_matrix

# Example Usage
# N = 5  # Number of nodes
graph_weights = list(W)  # Weights of the nodes (0-indexed)
adjacency_list = AM

# Get the all-pairs shortest path cost matrix
# result = calculate_all_pairs_cost(N, graph_weights, adjacency_list)
for r in range(1, N+1):
    nodes = combinations(range(N), r)
    print(r, list(nodes))
    costs = map(lambda x: W[x], nodes)
    cost = sum(costs)
    print(cost)