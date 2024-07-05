class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in matching:
                expected_open = matching[char]
                if stack and stack[-1] == expected_open:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return not stack