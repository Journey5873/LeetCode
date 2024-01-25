class Solution:
    def lengthOfLongestSubstring(self, s):
        dic = {}
        start, max_len = 0, 0

        for end in range(len(s)):
            
            if s[end] in dic and start <= dic[s[end]]:
                start = dic[s[end]] + 1
            dic[s[end]] = end
            max_len = max(max_len, len(s[start:end+1]))
        return max_len