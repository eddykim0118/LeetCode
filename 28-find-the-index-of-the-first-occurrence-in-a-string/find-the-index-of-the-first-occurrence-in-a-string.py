class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is an empty string, return 0
        if not needle:
            return 0
        
        # Helper function to compute the prefix function table
        def computeLPSArray(pattern: str):
            m = len(pattern)
            lps = [0] * m
            length = 0
            i = 1
            
            while i < m:
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        # Preprocess the needle to create the lps array
        lps = computeLPSArray(needle)
        
        i = 0  # index for haystack
        j = 0  # index for needle
        n = len(haystack)
        m = len(needle)
        
        while i < n:
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            
            if j == m:
                return i - j  # match found
            
            # mismatch after j matches
            elif i < n and needle[j] != haystack[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        
        return -1  # no match found

