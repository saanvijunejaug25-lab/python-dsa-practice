class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        final = []
        while left<right:
            w = right - left
            l = min(height[left],height[right])
            p = w*l 
            final.append(p)
            if height[left]<height[right]:
                left = left + 1
            else:
                right = right -1 
        return max(final)
        