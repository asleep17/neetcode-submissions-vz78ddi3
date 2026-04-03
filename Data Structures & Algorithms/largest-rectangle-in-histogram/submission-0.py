class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area=0
        for i in range(len(heights)):
            min_height = heights[i]
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                width = j - i + 1
                temp_area = min_height * width
                if temp_area > area:
                    area = temp_area
        return area