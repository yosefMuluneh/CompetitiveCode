class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        min_length = float('inf')
        window_sum = 0
        left = 0

        for right in range(n):
            window_sum += nums[right]  # Expand the window from the right

            # Shrink the window from the left until the sum is less than the target
            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0  # No subarray found
        else:
            return min_length