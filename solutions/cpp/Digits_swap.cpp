#include <iostream>
#include <vector>

using namespace std;

int main()
{
    char ch;
    int k, val;

    vector<vector<int>> freq(10, vector<int>());
    vector<char> digits;

    int i = 0;
    while (1)
    {
        cin >> ch;
        // if (ch == 32)
        //     break;
        cout << +ch << " ";
        // if (ch < '0' && ch > '9')
        //     // printf("Space\n");
        //     break;
        // val = ch - '0';
        // digits.push_back(val);
        // freq[val].push_back(i);
        // i++;
    }
    cin >> k;
    cout << k;
}