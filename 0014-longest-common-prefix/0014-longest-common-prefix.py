class Solution(object):
    def longestCommonPrefix(self, strs):
        
        if len(strs) == 0:
            return ""
        
        strs.sort(key=len, reverse=True)
        prefix = strs[0]

        for i in range(len(strs) - 1, -1, -1):
            curr = strs[i]
            shorter = min(len(prefix), len(curr))
            idx = shorter

            for j in range(shorter):
                if prefix[j] != curr[j]:
                    idx = j
                    break
            prefix = prefix[:idx]    

        return prefix
