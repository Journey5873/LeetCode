class Solution(object):
    def searchRange(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = last = mid
                while last + 1 <= len(nums) - 1 and nums[last + 1] == target:
                    last += 1
                while first - 1 >= 0 and nums[first - 1] == target:
                    first -= 1
                return [first, last]
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]