class Solution(object):
    def containsDuplicate(self, nums):
        duplicatedSet = set()
        
        for num in nums:
            if num in duplicatedSet:
                return True
            duplicatedSet.add(num)
        return False