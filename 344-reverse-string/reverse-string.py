from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Initialize two pointers
        left, right = 0, len(s) - 1

        # Swap characters until the pointers meet in the middle
        while left < right:
            # Swap the characters at left and right pointers
            s[left], s[right] = s[right], s[left]
            # Move the left pointer to the right
            left += 1
            # Move the right pointer to the left
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
