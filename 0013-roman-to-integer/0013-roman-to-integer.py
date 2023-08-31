class Solution(object):
    def romanToInt(self, s):
        romanDict = {"I": 1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000, "": 0}
        romanInt = 0
        temp = ""
        for i in range(len(s)-1, -1, -1):
            roman = s[i]
            if romanDict[temp] > romanDict[roman]:
                romanInt -= romanDict[roman]
            else:
                romanInt += romanDict[roman]
            temp = roman
        return romanInt
