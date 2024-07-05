class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> roman_to_int = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };

        int total = 0;
        int n = s.size();

        for (int i = 0; i < n; ++i) {
            if (i < n-1 && roman_to_int[s[i]] < roman_to_int[s[i+1]]) {
                total -= roman_to_int[s[i]];
            } else {
                total += roman_to_int[s[i]];
            }
        }
        return total;
    }
};