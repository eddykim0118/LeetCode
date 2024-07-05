class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charIndexMap;
        int left = 0;
        int maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            if (charIndexMap.find(s[right]) != charIndexMap.end()
            && charIndexMap[s[right]] >=left) {
                left = charIndexMap[s[right]] +1;
            }

            charIndexMap[s[right]] = right;
            maxLength = max(maxLength, right - left + 1);
        }
        return maxLength;
    }
};