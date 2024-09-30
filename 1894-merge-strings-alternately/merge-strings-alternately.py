class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize an empty list to store the result
        merged_string = []
        
        # Get the lengths of both words
        len1, len2 = len(word1), len(word2)
        
        # Loop over the length of the shorter word
        for i in range(min(len1, len2)):
            # Append alternating characters from both words
            merged_string.append(word1[i])
            merged_string.append(word2[i])
        
        # If word1 is longer, append the remaining part
        if len1 > len2:
            merged_string.append(word1[len2:])
        # If word2 is longer, append the remaining part
        elif len2 > len1:
            merged_string.append(word2[len1:])
        
        # Join the list into a string and return it
        return ''.join(merged_string)

