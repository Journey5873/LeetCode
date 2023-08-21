class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if x < INT_MIN or x > INT_MAX:
            return 0
        
        ret = 0
        is_negative = False
        
        if x < 0:
            is_negative = True
            x = -x
        
        while x:
            temp = x % 10
            ret = ret * 10 + temp
            x = x // 10
        
        if is_negative:
            ret = -ret
        
        if ret < INT_MIN or ret > INT_MAX:
            return 0
        
        return ret
