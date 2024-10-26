#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> adj;
vector<int> stars;
vector<int> dp;
// using dfs
int dfs(int city, int lastStar) {
    if (dp[city] != -1) return dp[city];
    int maxRestaurants = 1;

    for (int neighbor : adj[city]) {
        if (stars[neighbor] > lastStar) {
            maxRestaurants = max(maxRestaurants, 1 + dfs(neighbor, stars[neighbor]));
        }
    }
    return dp[city] = maxRestaurants;
}

int main() {
    int N;
    cin >> N;
    adj.resize(N + 1);
    stars.resize(N + 1);
    dp.assign(N + 1, -1);

    for (int i = 1; i <= N; i++) {
        cin >> stars[i];
    }

    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int maxPath = 0;
    for (int i = 1; i <= N; i++) {
        maxPath = max(maxPath, dfs(i, -1));
    }

    cout << maxPath << endl;
    return 0;
}
