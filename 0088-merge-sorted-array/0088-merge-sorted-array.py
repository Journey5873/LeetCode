class Solution(object):
    def merge(self, nums1, m, nums2, n):
        
        idx = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[idx]
            idx += 1
        nums1.sort ()
        return nums1