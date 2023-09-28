class Solution(object):
    def longestPalindrome(self, s):
        
        def isPalindrome(s):
            return s == s[::-1]

        for end in range(len(s), 0, -1):
            for start in range(0, len(s) - end + 1):
                subString = s[start:end+start]
                if isPalindrome(subString):
                    return subString
        return ""