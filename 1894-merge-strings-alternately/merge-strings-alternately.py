class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        min_len = min(len1, len2)
        merged = ''.join(word1[i] + word2[i] for i in range(min_len))
        if len1 > len2:
            return merged + word1[min_len:]
        else:
            return merged + word2[min_len:]