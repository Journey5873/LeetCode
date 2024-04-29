class Solution(object):
    def maxSubArray(self, nums):
        curr_sub = max_num = nums[0]

        for num in nums[1:]:
            if curr_sub + num < num:
                max_num = max(max_num, num)
                curr_sub = num
            else:
                curr_sub = curr_sub + num
                max_num = max(curr_sub, max_num)
            
        return max_num