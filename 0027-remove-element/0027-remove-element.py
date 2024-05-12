class Solution(object):
    def removeElement(self, nums, val):

        cnt = 0
        for i in range(len(nums)):
            if val != nums[i]:
                nums[cnt] = nums[i]
                cnt += 1
        return cnt
