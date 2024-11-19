def get_color(x, y):
    # To calculate the size of the triangle at each step
    size = [0] * 31
    size[1] = 2  # Base case size for step 1
    for n in range(2, 31):
        size[n] = 2 * size[n - 1] + 2  # Compute the size for steps 2 to 30
    
    # Determine the color of the point (x, y)
    while x > 1:
        prev_size = size[x - 1]  # Size of the previous step triangle
        if y <= prev_size:
            return 1  # It's red
        else:
            y -= prev_size + 1  # Move down to the next level
            x -= 1  # Move up to the previous level
    return 1  # The apex (1, 1) is always red

# Read number of queries
Q = int(input())
results = []
for _ in range(Q):
    x, y = map(int, input().split())
    results.append(get_color(x, y))

# Print results
print("\n".join(map(str, results)))