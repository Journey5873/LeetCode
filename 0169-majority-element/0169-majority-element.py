class Solution(object):
    def majorityElement(self, nums):
        majority_num = len(nums)//2
        num_dic = {}
        majority = nums[0]

        for num in nums:
            if num in num_dic:
                num_dic[num] += 1
            else:
                num_dic[num] = 1
            
            if num_dic[num] >= majority_num:
                if num_dic[majority] < num_dic[num]:
                    majority = num
        return majority