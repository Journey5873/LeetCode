class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        start, end = 0, len(nums1)

        while start <= end:

            partition_x = (start + end) // 2
            partition_y = (len(nums1) + len(nums2) + 1) // 2 - partition_x

            max_left_x = nums1[partition_x - 1] if partition_x != 0 else MIN_INT
            min_right_x = nums1[partition_x] if partition_x != len(nums1) else MAX_INT

            max_left_y = nums2[partition_y - 1] if partition_y != 0 else MIN_INT
            min_right_y = nums2[partition_y] if partition_y != len(nums2) else MAX_INT

            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y))/ 2.0
                else:
                    return max(max_left_x, max_left_y)
            elif max_left_x > min_right_y: # moves toward left in nums1 array
                end = partition_x - 1
            else: # moves toward right in nums1 array
                start = partition_x + 1