class Solution(object):
    def romanToInt(self, s):
        roman_dic = {"I": 1, "V": 5, "X": 10, "L": 50, 
                     "C": 100, "D": 500, "M": 1000}
        ret = 0
        idx = len(s) - 1

        prev = 2**31 - 1
        for i in range(len(s)):

            if prev < roman_dic[s[i]]:
                ret += roman_dic[s[i]]
                ret -= prev * 2
            else:
                ret += roman_dic[s[i]]

            prev = roman_dic[s[i]]

        return ret