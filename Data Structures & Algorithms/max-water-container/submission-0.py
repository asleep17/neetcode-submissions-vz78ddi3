class Solution:
    def maxArea(self, heights: List[int]) -> int:
        bottom=0
        top=len(heights)-1
        max_area=0
        while bottom<top:
            total_area=min(heights[bottom],heights[top])*(top-bottom)
            if total_area>max_area:
                max_area=total_area
            if heights[bottom]>heights[top]:
                top-=1
            else:
                bottom+=1
        return max_area
            
        