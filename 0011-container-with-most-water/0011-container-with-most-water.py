class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate current area
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            
            # Update max_area if needed
            max_area = max(max_area, current_area)

            # Move the pointer of the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area