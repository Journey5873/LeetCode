class Solution(object):
    def romanToInt(self, s):
        romanDict = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "": 0}
        prev = ""
        number = 0
        for i in range(len(s)-1, -1, -1):
            curr = s[i]
            if romanDict[prev] > romanDict[curr]:
                number -= romanDict[curr]
            else:
                number += romanDict[curr]
            prev = curr
        return number