class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        fromLeft = 0
        fromRight = len(height)-1
        
        while fromLeft < fromRight:
            width = fromRight-fromLeft
            min_height = min(height[fromLeft],height[fromRight])
            curr_area = width * min_height
            maxArea = max(maxArea,curr_area)
            
            if height[fromLeft]<height[fromRight]:
                fromLeft += 1
            else:
                fromRight -= 1
        return maxArea