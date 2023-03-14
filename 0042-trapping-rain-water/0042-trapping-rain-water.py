class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # initialize variables
        ans = 0 # total water trapped
        current = 0 # current index
        stack = [] # stack to store indices of bars

        while current < len(height):
            # if stack is not empty and current height is greater than previous height
            while stack and height[current] > height[stack[-1]]:
                # pop the top element of the stack
                top = stack.pop()
                # if stack is empty, break
                if not stack:
                    break
                # calculate the distance and bounded height
                distance = current - stack[-1] - 1
                bounded_height = min(height[current], height[stack[-1]]) - height[top]
                # update the answer by adding the water trapped
                ans += distance * bounded_height

            # push the current index to the stack
            stack.append(current)
            # move to the next index
            current += 1
    
        return ans