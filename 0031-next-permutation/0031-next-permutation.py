import itertools
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        
        #find pivot
        pivotIndex = -1
        swapNeed = False
        for i in range(size - 1, 0 , -1):
            if nums[i - 1] < nums[i]:
                pivotIndex = i - 1
                swapNeed = True
                break
        
        # find swapping number and swap with pivot
        if swapNeed:
            for i in range(size - 1, pivotIndex, -1):
                swapIndex = size - 1
                if nums[i] > nums[pivotIndex]:
                    swapIndex = i
                    break
        
            nums[swapIndex] , nums[pivotIndex] = nums[pivotIndex] , nums[swapIndex]

        # sorting the number right to pivot
        left = pivotIndex + 1
        right = size - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
