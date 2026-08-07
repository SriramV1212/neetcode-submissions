class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1

        area = 1

        while left<right:
            side_1 = min(heights[left],heights[right])
            side_2 = right - left
            new_area = side_1 * side_2

            if new_area > area:
                area = new_area
                if heights[left] > heights[right]:
                    right-=1
                else:
                    left+=1
            else:
                return(area)
                break

 





