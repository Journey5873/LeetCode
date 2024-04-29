class Solution(object):
    def maxSubArray(self, nums):
        curr_sub = max_num = nums[0]

        for num in nums[1:]:
            curr_sub = max(curr_sub + num, num)
            max_num = max(max_num, curr_sub)
        return max_num