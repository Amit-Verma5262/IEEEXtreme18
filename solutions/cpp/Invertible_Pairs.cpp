#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int testCases;
    cin >> testCases;
    while (testCases--) {
        int size;
        cin >> size;
        vector<int> array(size);
        for (int i = 0; i < size; ++i) {
            cin >> array[i];
        }

        vector<int> dpEven(size, 0);
        vector<int> dpOdd(size, 0);
        dpEven[0] = array[0];
        dpOdd[0] = -array[0];
        int maxResult = max(dpEven[0], dpOdd[0]);

        for (int i = 1; i < size; ++i) {
            if (i % 2 == 1) {
                dpEven[i] = max(dpEven[i - 1] + array[i], array[i]);
                dpOdd[i] = max(dpOdd[i - 1] - array[i], -array[i]);
            } else {
                int prevMax = max(dpEven[i - 1], dpOdd[i - 1]);
                dpEven[i] = max(prevMax + array[i], array[i]);
                dpOdd[i] = max(prevMax - array[i], -array[i]);
            }
            maxResult = max({maxResult, dpEven[i], dpOdd[i]});
        }
        cout << maxResult << endl;
    }
    return 0;
}