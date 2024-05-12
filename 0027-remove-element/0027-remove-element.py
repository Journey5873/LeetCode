class Solution(object):
    def removeElement(self, nums, val):

        idx = 0
        while idx < len(nums):
            if val == nums[idx]:
                nums.pop(idx)
                idx -= 1
            idx += 1
            
        return len(nums)
