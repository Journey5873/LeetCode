class Solution(object):
    def longestPalindrome(self, s):
        subString = ""
 
        def isPalindrome(sub):
            return sub == sub[::-1]
            
        for end in range(len(s), 0, -1):
            for start in range(0, len(s)-end+1):
                subString = s[start:start+end]
                if isPalindrome(subString):
                    return subString        
        return ""