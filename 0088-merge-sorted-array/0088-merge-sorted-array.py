class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for _ in range(len(nums1) - m):
            nums1.pop()
        nums1 += nums2
        nums1.sort()