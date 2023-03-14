class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2):
        # if nums1 is longer than nums2, swap them
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        # get the lengths of the two arrays
        m = len(nums1)
        n = len(nums2)
        # initialize the left and right pointers for binary search on nums1
        left = 0
        right = m
        # loop until the pointers converge
        while left <= right:
            # find the middle index of nums1 and its corresponding index in nums2
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            # find the four elements that may affect the median: maxLeftX, minRightX, maxLeftY, minRightY
            maxLeftX = float('-inf') if i == 0 else nums1[i - 1]
            minRightX = float('inf') if i == m else nums1[i]
            maxLeftY = float('-inf') if j == 0 else nums2[j - 1]
            minRightY = float('inf') if j == n else nums2[j]
            # check if we have found the correct partition: maxLeftX <= minRightY and maxLeftY <= minRightX
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # if the total length is odd, return the maximum of maxLeftX and maxLeftY as the median
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # else, return the average of the maximum of maxLeftX and maxLeftY and the minimum of minRightX and minRightY as the median 
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            # else, adjust the pointers based on which side is too small or too large 
            elif maxLeftX > minRightY:
                right = i - 1
            else:
                left = i + 1

        return -1