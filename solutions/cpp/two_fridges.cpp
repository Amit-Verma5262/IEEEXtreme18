#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> substances(n);
    for (int i = 0; i < n; ++i) {
        cin >> substances[i].first >> substances[i].second;
    }

    int max_lower_bound = -100;
    int min_upper_bound = 100;

    for (const auto &interval : substances) {
        max_lower_bound = max(max_lower_bound, interval.first);
        min_upper_bound = min(min_upper_bound, interval.second);
    }

    if (max_lower_bound <= min_upper_bound) {
        cout << max_lower_bound << " " << min_upper_bound << endl;
    } else {
        int T1 = -100;
        int T2 = 100;
        
        for (const auto &interval : substances) {
            if (interval.second < max_lower_bound) {
                T1 = max(T1, interval.second);
            } else if (interval.first > min_upper_bound) {
                T2 = min(T2, interval.first);
            }
        }
        
        if (T1 < T2) {
            cout << T1 << " " << T2 << endl;
        } else {
            cout << "-1" << endl;
        }
    }

    return 0;
}
