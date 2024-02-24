class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        start, end = 0, len(nums1)

        while start <= end:
            partition1 = (start + end) // 2
            partition2 = (len(nums1)+len(nums2)+1) // 2 - partition1

            max_left_1 = nums1[partition1 - 1] if partition1 != 0 else float("-inf")
            min_right_1 = nums1[partition1] if partition1 != len(nums1) else float("inf")

            max_left_2 = nums2[partition2-1] if partition2 != 0 else float("-inf")
            min_right_2 = nums2[partition2] if partition2 != len(nums2) else float("inf")

            if max_left_1 <= min_right_2 and max_left_2 <= min_right_1:
                if (len(nums1)+len(nums2)) % 2 == 0:
                    return (float(max(max_left_1, max_left_2)) + float(min(min_right_1, min_right_2))) / 2.0
                else:
                    return float(max(max_left_1, max_left_2) )
            elif max_left_1 > min_right_2:
                end = partition1 - 1
            else:
                start = partition1 + 1