class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_str = ''
        
        for char in s:
            if char.isalnum():
                new_str += char.lower()
        
        return new_str == new_str[::-1]