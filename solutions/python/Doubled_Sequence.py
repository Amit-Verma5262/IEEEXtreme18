def construct_sequence(N):
    if N % 2 != 0:
        return "-1"  # No valid sequence for odd N

    # Generate sequence for even N
    sequence = [0] * (2 * N)
    pos = 0
    for i in range(1, N + 1):
        sequence[pos] = i
        # Ensure pos + i + 1 is within bounds of the list
        if pos + i + 1 < len(sequence):
            sequence[pos + i + 1] = i
        pos += 1
    return ' '.join(map(str, sequence))

# Reading input
import sys
input = sys.stdin.read
data = input().split()
T = int(data[0])
results = []
for idx in range(1, T + 1):
    N = int(data[idx])
    results.append(construct_sequence(N))

# Print all results at once
sys.stdout.write("\n".join(results) + "\n")