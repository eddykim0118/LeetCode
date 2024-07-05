class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charIndexMap ={}
        left = 0
        maxLength =0

        for right in range(len(s)):
            if s[right] in charIndexMap and charIndexMap[s[right]] >= left:
                left = charIndexMap[s[right]] + 1
            
            charIndexMap[s[right]] = right
            maxLength = max(maxLength, right - left +1)

        return maxLength        