class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
       # Brute force
       
        # size = len(heights)
        # maxArea = 0

        # for i in range(size):
        #     minHeight = heights[i]
        #     for j in range(i, size):
        #         minHeight = min(minHeight , heights[j])
        #         area = minHeight * (j -i + 1)
        #         maxArea = max(maxArea , area)
        
        # return maxArea


        # optimal approach

        size = len(heights)
        left = [0]*size
        right = [0]*size
        stack = []

        # right smaller

        for i in range(size-1 , -1 , -1 ):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                right[i] = size
            else:
                right[i] = stack[-1]

            stack.append(i)

        while stack:
            stack.pop()

             # left smaller

        for i in range(size):

            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
                
            stack.append(i)

        maxArea = 0
        for i in range(size):
            area = heights[i] * (right[i] - left[i] - 1)
            maxArea = max(maxArea , area)
        
        return maxArea