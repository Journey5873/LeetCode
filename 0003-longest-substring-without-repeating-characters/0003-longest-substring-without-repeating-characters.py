class Solution:
    def lengthOfLongestSubstring(self, s):
        start = 0
        dic = {}
        max_len = 0

        for end in range(len(s)) :
            if s[end] in dic and start <= dic[s[end]] + 1:
                start = dic[s[end]] + 1

            cur_len = len(s[start:end+1])
            max_len = max(max_len, cur_len)

            dic[s[end]] = end
        return max_len
    