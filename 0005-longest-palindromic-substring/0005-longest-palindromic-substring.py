class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s
        
        start = 0
        max_length = 1
        
        dp = [[False] * n for _ in range(n)]
        
        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_length = 2
        
        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if length > max_length:
                        start = i
                        max_length = length
        
        return s[start:start + max_length]
