class Solution(object):
    def twoSum(self, nums, target):
        # make a set
        numSet =  set()
        
        # make output list
        output = []

        # check the nums list
        for i in range(len(nums)):
            num = target - nums[i]
            if num in numSet:
                output.append(i)
                output.append(nums.index(num))
                return output
            numSet.add(nums[i]) 
            
        # no solution found
        return []
            

            
            

        

