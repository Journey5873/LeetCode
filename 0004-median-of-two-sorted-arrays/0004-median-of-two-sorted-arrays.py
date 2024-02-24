class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        lst = nums1 + nums2
        lst.sort()

        if len(lst) % 2 == 0:
            return (float(lst[len(lst)//2]) + float(lst[len(lst)//2 - 1])) / 2.0
        else:
            return float(lst[len(lst)//2])
