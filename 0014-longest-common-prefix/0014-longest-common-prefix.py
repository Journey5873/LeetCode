class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = ""

        prefix = strs[0]
        for i in range(1, len(strs)):
            j=0
            currentWord = strs[i]
            while j < len(currentWord) and j < len(prefix):
                if currentWord[j] != prefix[j]:
                    break
                j += 1
            prefix = prefix[0:j]
        
        if len(prefix) == 0:
            return ""
        return prefix