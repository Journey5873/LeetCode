class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        threeSumList = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    threeSumList.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                    right -= 1
                    left += 1
                if sum < 0:
                    left += 1
                if sum > 0:
                    right -= 1
        return threeSumList