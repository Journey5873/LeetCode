class Solution(object):
    def removeDuplicates(self, nums):
        idx = 0

        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                idx+=1
                nums[idx] = nums[i+1]
        return idx + 1
