class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        threeSumList = []
        closestNum = float('inf')

        for i in range(len(nums)-2):
            if i < 0 and nums[i] == nums[i-1]:
                continue

            mid, end = i + 1, len(nums) -1 

            while mid < end :
                threeSum = nums[i] + nums[mid] + nums[end]
                closestNum = self.findClosesrNumber(target, threeSum, closestNum)

                if threeSum == target:
                    closestNum = threeSum
                    return closestNum
                if threeSum < target:
                    mid += 1
                if threeSum > target:
                    end -= 1

        return closestNum


    def findClosesrNumber(self, target, num1, num2):
        diff1 = abs(target - num1)
        diff2 = abs(target - num2)
        
        if diff1 < diff2:
            return num1
        elif diff2 < diff1:
            return num2
        else:
            return num1