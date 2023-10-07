class Solution:
    def lengthOfLongestSubstring(self, s):
        maxLength = start = 0
        dic = {}

        for end in range(len(s)):
            if s[end] in dic and start <= dic[s[end]]:
                start = dic[s[end]] + 1
            maxLength = max(maxLength, end - start + 1)
            dic[s[end]] = end
        return maxLength