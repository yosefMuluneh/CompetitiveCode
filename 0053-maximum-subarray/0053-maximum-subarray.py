class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totlMax = nums[0]
        curMax = nums[0]
        for i in range(1,len(nums)):
            curMax = max(curMax+nums[i],nums[i])
            totlMax = max(totlMax,curMax)

        return totlMax
        