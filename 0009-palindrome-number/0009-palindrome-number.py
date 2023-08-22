class Solution(object):
    def isPalindrome(self, x):
        numStr = str(x)
        return numStr == numStr[::-1]