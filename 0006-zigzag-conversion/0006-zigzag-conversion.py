class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        list = [''] * numRows 
        idx, step = 0, 1
        
        for c in s:
            list[idx] += c
            
            if idx == 0:
                step = 1
            elif idx == numRows -1 :
                step = -1
            idx += step

        return ''.join(list)