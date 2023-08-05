class Solution:
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        start = 0
        charIndexMap = {}

        for end in range(len(s)):
            if s[end] in charIndexMap and charIndexMap[s[end]] >= start:
                start = charIndexMap[s[end]] + 1
            charIndexMap[s[end]] = end
            maxLength = max(maxLength, end - start + 1)

        return maxLength