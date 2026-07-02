class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # 1. Sort the array so we can use pointers and easily skip duplicates
        nums.sort()
        
        for i in range(len(nums)):
            # 2. Skip duplicate values for our main anchor (i)
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # 3. Set up two pointers: one right after 'i', one at the end of the list
            left = i + 1
            right = len(nums) - 1
            
            # 4. Move pointers inward to find sums
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum > 0:
                    # Sum is too big, move the right pointer to a smaller number
                    right -= 1
                elif three_sum < 0:
                    # Sum is too small, move the left pointer to a bigger number
                    left += 1
                else:
                    # We found exactly 0!
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer forward, skipping any duplicates along the way
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return res