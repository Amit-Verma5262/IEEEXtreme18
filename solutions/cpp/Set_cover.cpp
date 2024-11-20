#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>

using namespace std;


int minimum_reading_time(vector<pair<int, set<string>>>& books) {
    
    set<string> all_topics;
    for (auto& book : books) {
        all_topics.insert(book.second.begin(), book.second.end());
    }

    int n = books.size();
    int min_time = INT_MAX; 


    for (int mask = 1; mask < (1 << n); ++mask) {
        set<string> covered_topics;
        int total_time = 0;
        
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) { 
                total_time += books[i].first; 
                covered_topics.insert(books[i].second.begin(), books[i].second.end()); // Añadir los temas cubiertos
            }
        }

        // Verificamos si cubrimos todos los temas
        if (covered_topics == all_topics) {
            min_time = min(min_time, total_time); // Actualizamos el tiempo mínimo
        }
    }

    return min_time;
}

int main() {
    
    vector<pair<int, set<string>>> books = {
        {300, {"Backtracking", "Dynamic_Programming", "Greedy"}},
        {125, {"Dynamic_Programming"}},
        {35,  {"Backtracking"}},
        {85,  {"Greedy"}},
        {120, {"Backtracking", "Dynamic_Programming"}},
        {80,  {"Greedy", "Backtracking"}}
    };


    int result = minimum_reading_time(books);
    
    cout << result << endl;

    return 0;
}