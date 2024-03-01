class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ""
        
        prefix = strs[0]

        for i in range(1, len(strs)):
            current_word = strs[i]
            shorter_word_len = min(len(current_word), len(prefix))

            j = 0
            while j < shorter_word_len:
                if prefix[j] != current_word[j]:
                    break
                j += 1
            prefix = prefix[:j]
            
            if not prefix:
                break  
            
        return prefix
    