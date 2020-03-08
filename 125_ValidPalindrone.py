# Link : https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text = [c if(c.isalpha() or c.isnumeric()) else '' for c in s.lower()]
        r_str = ''.join(text)
        return r_str == r_str[::-1]
