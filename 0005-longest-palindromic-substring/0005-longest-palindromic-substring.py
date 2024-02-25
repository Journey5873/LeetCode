class Solution(object):
    def longestPalindrome(self, s):

        max_s, max_e = 0, 0

        for i in range(len(s)):

            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if max_e - max_s < end - start:
                    max_s, max_e = start, end
                start, end = start - 1, end + 1

            start, end = i, i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if max_e - max_s < end - start:
                    max_s, max_e = start, end
                start, end = start - 1, end + 1
        return s[max_s : max_e + 1]