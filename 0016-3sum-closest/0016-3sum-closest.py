class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closestSum = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]

                if currentSum == target:
                    return target

                if abs(currentSum - target) < abs(closestSum - target):
                    closestSum = currentSum

                if currentSum < target:
                    left += 1
                else:
                    right -= 1

        return closestSum
