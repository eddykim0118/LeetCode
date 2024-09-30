class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = []
        
        len1, len2 = len(word1), len(word2)
        
        for i in range(min(len1, len2)):
            merged_string.append(word1[i])
            merged_string.append(word2[i])
        
        if len1 > len2:
            merged_string.append(word1[len2:])
        elif len2 > len1:
            merged_string.append(word2[len1:])
        
        return ''.join(merged_string)

