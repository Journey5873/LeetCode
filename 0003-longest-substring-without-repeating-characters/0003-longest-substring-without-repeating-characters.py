class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        maxLenght = 0

        start = 0
        for end in range(len(s)):
            if s[end] in dic and start <= dic[s[end]]:
                start = dic[s[end]] + 1
            dic[s[end]] = end
            maxLenght = max(maxLenght, len(s[start:end+1]))
        return maxLenght