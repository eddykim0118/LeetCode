class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words_list = s.split() 
        reversed_words = words_list[::-1]
        return " ".join(reversed_words)