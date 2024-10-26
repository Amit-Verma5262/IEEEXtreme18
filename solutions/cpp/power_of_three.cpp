#include <bits/stdc++.h>
using namespace std;

int main() {
    long long N;
    cin >> N;

    if (N < 1) {
        cout << -1 << endl;
        return 0;
    }

    double log3_N = log10(N) / log10(3);
    int x = round(log3_N);

    // Check if 3^x is approximately equal to N within a small tolerance
    if (abs(pow(3, x) - N) < 1e-9) {
        cout << x << endl;
    } else {
        cout << -1 << endl;
    }

    return 0;
}
