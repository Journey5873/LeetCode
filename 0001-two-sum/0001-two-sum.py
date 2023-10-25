class Solution(object):
    def twoSum(self, nums, target):
        diffDic = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diffDic:
                return [diffDic[diff], i]
            diffDic[nums[i]] = i
        return []