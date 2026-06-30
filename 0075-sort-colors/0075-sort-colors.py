class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first = 0
        last = len(nums) -1 
        pointer = 0

        while pointer<=last:

            if nums[pointer] == 0:
                nums[pointer], nums[first] = nums[first], nums[pointer]
                first += 1
                pointer += 1
                
            elif nums[pointer] == 2:
                nums[pointer], nums[last] = nums[last], nums[pointer]
                last -= 1
                # Notice there is NO pointer += 1 here!
                
            else:
                pointer += 1

