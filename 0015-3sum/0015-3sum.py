class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ret = []

        for i in range(len(nums)-2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            curr = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if curr + nums[left] + nums[right] == 0:
                    ret.append([curr, nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif curr + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return ret