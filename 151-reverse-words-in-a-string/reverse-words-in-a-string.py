class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split() 
        reversed_words = words_list[::-1]
        return " ".join(reversed_words)


