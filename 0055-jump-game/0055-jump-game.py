class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_position = len(nums) - 1

        # Iterate over the array in reverse order
        for i in range(len(nums) - 2, -1, -1):
            # Check if the current position can reach the last position
            if i + nums[i] >= last_position:
                last_position = i

        # If the last position is 0, it means we can reach the last index
        return last_position == 0      