class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        width = right-left

        max_area = 0
        while(left!=right):
            area_left = heights[left]
            area_right = heights[right]
            area_curr = min(heights[left],heights[right])*width
            max_area = max(max_area, area_curr)
            if(area_left<area_right):
                left+=1
            else: 
                right-=1
            width = right-left
        return max_area