class Solution(object):
    def moveZeroes(self, nums):
        index = count = 0
        while count < len(nums):
            if nums[index] == 0:
                nums.append(0)
                nums.pop(index)
            else: 
                index += 1
            count += 1