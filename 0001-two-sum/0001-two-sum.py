class Solution(object):
    def twoSum(self, nums, target):
        # make a set to store complements
        numSet =  set()

        # check the nums list
        for i in range(len(nums)):
            num = target - nums[i]
            if num in numSet:
                return [i, nums.index(num)]
            numSet.add(nums[i]) 
            
        # no solution found
        return []
            

            
            

        

