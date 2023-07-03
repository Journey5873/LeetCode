class Solution(object):
    def moveZeroes(self, nums):
        noneZeroIndex = 0
        
        for num in nums:
            if num != 0:
                nums[noneZeroIndex] = num
                noneZeroIndex += 1
        for i in range(noneZeroIndex, len(nums)):
            nums[i] = 0
        
        return nums