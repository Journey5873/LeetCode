class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(0, len(nums1)-m):
            nums1.pop()
        nums1.extend(nums2)
        nums1.sort()
        
        