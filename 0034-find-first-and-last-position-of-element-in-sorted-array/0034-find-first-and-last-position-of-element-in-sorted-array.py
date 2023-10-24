class Solution(object):
    def searchRange(self, nums, target):
        def lowerBound(left, right):
            while left < right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return right
        def uppperBound(left, right):
            while left < right:
                mid = (left+right)//2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return right - 1
        
        first = lowerBound(0, len(nums))
        last = uppperBound(0, len(nums))
        if first > last:
            return[-1,-1]
        return [first, last]