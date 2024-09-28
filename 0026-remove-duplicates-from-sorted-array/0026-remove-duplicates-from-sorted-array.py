class Solution(object):
    def removeDuplicates(self, nums):
        idx = 0
        duplicated = {}

        for i in range(len(nums)):
            if nums[i] not in duplicated:
                nums[idx] = nums[i]
                duplicated[nums[i]] = True
                idx += 1
        return idx