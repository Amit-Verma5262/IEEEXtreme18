#include <bits/stdc++.h>
using namespace std;

struct Project {
    int id;
    int group;
    Project(int id, int group) : id(id), group(group) {}
    bool operator<(const Project &other) const {
        if (group == other.group) return id > other.id;
        return group > other.group;
    }
};

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> group_id(n);
    vector<vector<int>> adj(n);
    vector<int> in_degree(n, 0);
    
    for (int i = 0; i < n; ++i) {
        cin >> group_id[i];
    }

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        --a; --b;
        adj[a].push_back(b);
        in_degree[b]++;
    }

    priority_queue<Project> pq;
    
    for (int i = 0; i < n; ++i) {
        if (in_degree[i] == 0) {
            pq.emplace(i, group_id[i]);
        }
    }

    vector<int> result;

    while (!pq.empty()) {
        auto [current, group] = pq.top(); pq.pop();
        result.push_back(current + 1);

        for (int neighbor : adj[current]) {
            if (--in_degree[neighbor] == 0) {
                pq.emplace(neighbor, group_id[neighbor]);
            }
        }
    }

    if (result.size() != n) {
        cout << -1 << endl;
    } else {
        for (int proj : result) {
            cout << proj << " ";
        }
        cout << endl;
    }

    return 0;
}
