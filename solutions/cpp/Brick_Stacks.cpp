#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    int totalBricks;
    long long minGap;
    cin >> totalBricks >> minGap;
    vector<long long> brickSizes(totalBricks);
    
    for (int i = 0; i < totalBricks; ++i) {
        cin >> brickSizes[i];
    }

    sort(brickSizes.begin(), brickSizes.end());

    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<>> stackQueue;

    vector<vector<long long>> stacks;

    for (long long currentBrick : brickSizes) {
        if (!stackQueue.empty() && stackQueue.top().first + minGap <= currentBrick) {

            int stackIdx = stackQueue.top().second;
            stackQueue.pop();
            stacks[stackIdx].push_back(currentBrick);
            stackQueue.emplace(currentBrick, stackIdx);
        } else {
            stacks.push_back({currentBrick});
            stackQueue.emplace(currentBrick, stacks.size() - 1);
        }
    }

    cout << stacks.size() << endl;
    for (const auto &stack : stacks) {
        cout << stack.size();
        for (auto it = stack.rbegin(); it != stack.rend(); ++it) {
            cout << " " << *it;
        }
        cout << endl;
    }

    return 0;
}