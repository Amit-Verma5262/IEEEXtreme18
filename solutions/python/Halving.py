MOD = 998244353

def count_valid_permutations(N, C, R, B):
    possible_values = set(range(1, 2 * N + 1))

    for val in C:
        if val != -1:
            possible_values.discard(val)
    
    possible_values = sorted(possible_values)
    dp = [{} for _ in range(N + 1)]
    dp[0][()] = 1

    for i in range(1, N + 1):
        min_max = R[i - 1]
        target_b = B[i - 1]

        val1, val2 = C[2 * i - 2], C[2 * i - 1]
        candidates = []

        if val1 != -1 and val2 != -1:
            candidates = [(val1, val2)]
        elif val1 != -1:
            candidates = [(val1, v) for v in possible_values if v != val1]
        elif val2 != -1:
            candidates = [(v, val2) for v in possible_values if v != val2]
        else:
            candidates = [(v1, v2) for v1 in possible_values for v2 in possible_values if v1 != v2]

        valid_candidates = []
        for v1, v2 in candidates:
            if (min_max == 0 and min(v1, v2) == target_b) or (min_max == 1 and max(v1, v2) == target_b):
                valid_candidates.append((v1, v2))

        new_dp = {}
        for state, count in dp[i - 1].items():
            for v1, v2 in valid_candidates:
                if v1 not in state and v2 not in state:
                    new_state = tuple(sorted(state + (v1, v2)))
                    if new_state in new_dp:
                        new_dp[new_state] = (new_dp[new_state] + count) % MOD
                    else:
                        new_dp[new_state] = count % MOD
        dp[i] = new_dp

    return sum(dp[N].values()) % MOD

# Read input values
N = int(input().strip())
C = list(map(int, input().strip().split()))
R = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

# Compute the result and print it
result = count_valid_permutations(N, C, R, B)
print(result)