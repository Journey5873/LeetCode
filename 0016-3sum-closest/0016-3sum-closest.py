class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestSum = float('inf')

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == target:
                    return target

                if abs(sum - target) < abs(closestSum - target):
                    closestSum = sum
                if sum < target:
                    left += 1
                if sum > target:
                    right -= 1
        return closestSum
