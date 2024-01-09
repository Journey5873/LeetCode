class Solution(object):
    def nthUglyNumber(self, n):
        
        ugly_numbers = [1]

        
        i2, i3, i5 = 0, 0, 0

        while len(ugly_numbers) < n:
            
            next_ugly2 = ugly_numbers[i2] * 2
            next_ugly3 = ugly_numbers[i3] * 3
            next_ugly5 = ugly_numbers[i5] * 5

            next_ugly = min(next_ugly2, next_ugly3, next_ugly5)

            ugly_numbers.append(next_ugly)

            if next_ugly == next_ugly2:
                i2 += 1
            if next_ugly == next_ugly3:
                i3 += 1
            if next_ugly == next_ugly5:
                i5 += 1

        return ugly_numbers[-1]