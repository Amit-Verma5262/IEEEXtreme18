#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

const int MOD = 998244353;

// Function to calculate factorial modulo MOD
int factorial(int n) {
    long long result = 1;
    for (int i = 1; i <= n; ++i) {
        result = (result * i) % MOD;
    }
    return result;
}

// Function to count valid permutations
int countValidPermutations(int N, vector<int>& C, vector<int>& R, vector<int>& B) {
    vector<bool> used(2 * N + 1, false); // Track which numbers are fixed
    unordered_set<int> missing;          // Track numbers that can be placed
    
    // Mark used numbers and identify missing numbers
    for (int i = 0; i < 2 * N; ++i) {
        if (C[i] != -1) used[C[i]] = true;
    }
    for (int i = 1; i <= 2 * N; ++i) {
        if (!used[i]) missing.insert(i);
    }
    
    int ways = 1; // Total ways to assign missing values in pairs
    
    for (int i = 0; i < N; ++i) {
        int pos1 = 2 * i;
        int pos2 = 2 * i + 1;
        
        if (R[i] == 0) { // Rule R[i] = 0, so B[i] should be the minimum
            int min_val = B[i];
            if (C[pos1] != -1 && C[pos2] != -1) { // Both positions are known
                if (min(C[pos1], C[pos2]) != min_val) return 0;
            } else if (C[pos1] == min_val || C[pos2] == min_val) {
                missing.erase(min_val); // This value has been used
            } else if (missing.count(min_val)) {
                ways = (ways * 1) % MOD; // Only 1 way to assign min
                missing.erase(min_val);  // Remove from missing
            } else {
                return 0;
            }
        } else { // Rule R[i] = 1, so B[i] should be the maximum
            int max_val = B[i];
            if (C[pos1] != -1 && C[pos2] != -1) { // Both positions are known
                if (max(C[pos1], C[pos2]) != max_val) return 0;
            } else if (C[pos1] == max_val || C[pos2] == max_val) {
                missing.erase(max_val); // This value has been used
            } else if (missing.count(max_val)) {
                ways = (ways * 1) % MOD; // Only 1 way to assign max
                missing.erase(max_val);  // Remove from missing
            } else {
                return 0;
            }
        }
    }
    
    // Multiply by factorial of remaining missing numbers
    ways = (ways * factorial(missing.size())) % MOD;
    return ways;
}

int main() {
    int N;
    cin >> N;
    
    vector<int> C(2 * N);
    for (int i = 0; i < 2 * N; ++i) {
        cin >> C[i];
    }
    
    vector<int> R(N);
    for (int i = 0; i < N; ++i) {
        cin >> R[i];
    }
    
    vector<int> B(N);
    for (int i = 0; i < N; ++i) {
        cin >> B[i];
    }
    
    int result = countValidPermutations(N, C, R, B);
    cout << result << endl;

    return 0;
}