class Solution:
    def lengthOfLongestSubstring(self, s):
        maxLenght = 0 
        start = 0
        lastIndex = {}

        for end in range(len(s)):
            if s[end] in lastIndex and start <= lastIndex[s[end]]:
                start = lastIndex[s[end]] + 1
            lastIndex[s[end]] = end
            maxLenght = max(maxLenght, end - start + 1)
        return maxLenght
