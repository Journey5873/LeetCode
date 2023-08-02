class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLength = 0
        length = 0
        idx = 0

        for i in range(0, len(s)):
            length = 0
            dic = {}
            for char in s[i:]:
                if char in dic:
                    break
                else:
                    dic[char] = idx
                idx += 1
                length += 1
            if length > maxLength:
                maxLength = length
        return maxLength