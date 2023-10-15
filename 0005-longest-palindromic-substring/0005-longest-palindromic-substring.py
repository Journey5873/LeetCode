class Solution(object):
    def longestPalindrome(self, s):
        def isPalindrome(s):
            return s == s[::-1]
        
        for end in range(len(s), 0, -1):
            for start in range(0, len(s)-end+1):
                if isPalindrome(s[start:start+end]):
                    return s[start:start+end]
        return ""