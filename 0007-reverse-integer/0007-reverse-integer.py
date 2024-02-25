class Solution(object):
    def reverse(self, x):
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        is_nagative = True if x < 0 else False
        revers_x = 0

        x = abs(x)
        while x:
            revers_x = (10 * revers_x) + (x % 10)
            x = x // 10

        revers_x = revers_x if not is_nagative else revers_x * -1

        if revers_x >= MAX_INT or revers_x <= MIN_INT:
            return 0
        return revers_x