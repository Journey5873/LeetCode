class Solution(object):
    def rotate(self, nums, k):
        if k == 0:
            return nums
        k = k % len(nums)  
        nums.reverse()
        nums[:k] = list(reversed(nums[:k])) 
        nums[k:] = list(reversed(nums[k:]))
        return nums