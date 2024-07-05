from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1  # Initialize two pointers
        
        while left < right:
            # Swap characters using tuple unpacking, which can be more efficient in Python
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Example usage:
solution = Solution()

# Test case 1
s1 = ["h", "e", "l", "l", "o"]
solution.reverseString(s1)
print(s1)  # Output: ["o", "l", "l", "e", "h"]

# Test case 2
s2 = ["H", "a", "n", "n", "a", "h"]
solution.reverseString(s2)
print(s2)  # Output: ["h", "a", "n", "n", "a", "H"]
