#include <iostream>
#include <vector>

int main() {
    int n, k;
    std::cin >> n >> k;
    
    std::vector<int> e_balls(k);
    for (int i = 0; i < k; i++) {
        std::cin >> e_balls[i];
    }
    
    int count = 0;
    for (int i = 1; i <= n; i++) {
        for (int e : e_balls) {
            if (i % e == 0) {
                count++;
                break;
            }
        }
    }
    
    std::cout << count << std::endl;
    return 0;
}