class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        left, right = 0, 0

        while right < len(heights):

            area = min(heights[left],heights[right]) * (right-left)

            max_area = max(area,max_area)

            if heights[right] > heights[left]:
                left = right

            right+=1

        return max_area
        