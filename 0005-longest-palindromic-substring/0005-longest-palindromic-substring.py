class Solution(object):
    def longestPalindrome(self, s):
        maxStart, maxEnd = 0, 0

        for i in range(len(s)):
            start, end = i, i
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if maxEnd - maxStart < end - start:
                    maxStart, maxEnd = start, end
                start, end = start - 1, end + 1

            start, end = i, i + 1
            while 0 <= start and end < len(s) and s[start] == s[end]:
                if maxEnd - maxStart < end - start:
                    maxStart, maxEnd = start, end
                start, end = start - 1, end + 1
        return s[maxStart:maxEnd+1]