class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        isNegative = False

        if x < INT_MIN or x > INT_MAX:
            return 0

        if x < 0:
            isNegative = True
            x = -x

        ret = 0
        while x :
            temp = x % 10
            ret = ret * 10 + temp
            x = x //10
        
        if isNegative:
            ret = -ret

        if ret < INT_MIN or ret > INT_MAX:
            return 0
        
        return ret