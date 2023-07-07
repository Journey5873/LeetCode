class Solution(object):
    def containsDuplicate(self, nums):
        numsCounter = Counter(nums)
        
        for count in numsCounter.values():
            if count > 1:
                return True
        return False
        
        