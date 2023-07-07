class Solution(object):
    def containsDuplicate(self, nums):
        numsCounts = Counter(nums)
        
        for count in numsCounts.values():
            if count > 1:
                return True
        return False