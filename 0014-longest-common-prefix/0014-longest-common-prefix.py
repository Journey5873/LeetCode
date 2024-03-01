class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]

        for i in range(1, len(strs)):
            current_word = strs[i]

            j = 0
            while j < len(prefix) and j < len(current_word) and prefix[j] == current_word[j]:
                j += 1

            prefix = prefix[:j]
            
            if not prefix:
                break  
            
        return prefix
    